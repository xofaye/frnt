import logging


from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from jsonview.decorators import json_view
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect

from .services import furniture_search
from .forms import SignUpForm, SearchFurnitureForm, EditProfileForm, LocationForm, \
    AddListingForm, EditListingForm, ListingPictureForm
from .models import Listing, Location, Profile, ListingPicture


class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def home(request):
    args = {}
    args['search_form'] = SearchFurnitureForm()

    return render(request, 'index.html', args)


def dashboard(request):
    my_listings = Listing.objects.filter(user=request.user.profile)
    listings = Listing.objects.all().order_by('-id')[:6]
    context = {'listings': listings, 'my_listings': my_listings}
    return render(request, 'dashboard.html', context)


def all_listings(request):
    listings = Listing.objects.all().order_by('-id')
    context = {'listings': listings}
    return render(request, 'all_listings.html', context)


def logout_success(request):
    logout(request)
    return render(request, 'logout_success.html')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return redirect('login')
    args = {}
    #args.update(csrf(request))
    args['form'] = SignUpForm()
    return render(request, 'register.html', args)

@json_view
def search_furniture(request):
    if request.method == 'POST':
        form = SearchFurnitureForm(request.POST)
        if form.is_valid():
            query_params = {}
            query_params['title__icontains'] = form.cleaned_data['query']
            if form.cleaned_data['min_price']:
                query_params['price__gte'] = form.cleaned_data['min_price']
            if form.cleaned_data['max_price']:
                query_params['price__lte'] = form.cleaned_data['max_price']
            if form.cleaned_data['location']:
                query_params['location__city__icontains'] = form.cleaned_data['location']

            query_set = Listing.objects.filter(**query_params)

            return render(request, 'listings.html', {'form': form, 'data': query_set})

    args = {}
    args['form'] = SearchFurnitureForm()
    return render(request, 'search.html', args)


def edit_profile(request):
    l = None
    loc_form = LocationForm(request.POST or None)
    form = EditProfileForm(request.POST or None)
    if request.method == 'POST':
        if loc_form.is_valid():
            street_address = loc_form.cleaned_data['street_address']
            city = loc_form.cleaned_data['city']
            postal_code = loc_form.cleaned_data['postal_code']
            country = loc_form.cleaned_data['country']
            if street_address or city or postal_code or country:
                l = Location.objects.create(street_address=street_address, city=city,
                                        postal_code=postal_code, country=country)
        profile = request.user.profile
        if form.is_valid():
            if l:
                profile.location = l
            profile.profile_image = form.cleaned_data['profile_image']
            profile.biography = form.cleaned_data['biography']
            profile.save()
            return redirect('home')
    return render(request, 'edit_profile.html', {'form': form, 'loc_form': loc_form})


def view_profile(request, username):
    profile = get_object_or_404(Profile, user__username__iexact=username)
    listings = Listing.objects.filter(user=profile)
    context = {'user': request.user, 'profile': profile, 'listings': listings}
    return render(request, 'view_profile.html', context)


def view_listing(request, id):
    listing = get_object_or_404(Listing, id__iexact=id)

    approve_alert = int(request.GET.get('accept', 0)) == 1
    if approve_alert:
        title = listing.title
        subject = 'Booking Request Approved!'
        project_email = 'csc301project@freeatnet.com'
        to_email = request.GET.get('requester_email', '')
        email_text = "Hi there! <br><br>" + "Your request for " + title + " has been approved!" + "We hope you enjoy it!"
        msg = EmailMessage(subject, email_text, project_email, [to_email])
        msg.content_subtype = "html"
        msg.send()


    context = {'user': request.user, 'listing': listing, 'approve_alert': approve_alert}
    return render(request, 'view_listing.html', context)


def add_listing(request):
    loc_form = LocationForm(request.POST or None)
    form = AddListingForm(request.POST or None)
    pic_form = ListingPictureForm(request.POST or None)

    if request.method == 'POST':
        if loc_form.is_valid():
            street_address = loc_form.cleaned_data['street_address']
            city = loc_form.cleaned_data['city']
            postal_code = loc_form.cleaned_data['postal_code']
            country = loc_form.cleaned_data['country']

            l = None
            listing = None
            if street_address or city or postal_code or country:
                l = Location.objects.create(street_address=street_address, city=city,
                                            postal_code=postal_code, country=country)

            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                price = form.cleaned_data['price']
                listing = Listing.objects.create(title=title, description=description,
                                                 price=price, location=l, user=request.user.profile)
            title, url = None, None
            if pic_form.is_valid():
                url = pic_form.cleaned_data['url']
            listing.pictures.add(ListingPicture.objects.create(title='Title', url=url))
            context = {'user': request.user, 'listing': listing}
            return render(request, 'view_listing.html', context)

    context = {
        'form': form,
        'loc_form': loc_form,
        'pic_form': pic_form
    }
    return render(request, 'add_listing.html', context)


def edit_listing(request):
    if request.method == 'POST':
        form = EditListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': EditListingForm()
    }
    return render(request, 'edit_listing.html', context)


def book(request):
    subject = 'New Furniture Booking'
    listing_id = request.POST.get('id', 0)
    title = request.POST.get('title', '')
    name = request.POST.get('first_name', '')
    username = request.POST.get('username', '')

    message = request.POST.get('booking_message', '')
    project_email = 'csc301project@freeatnet.com'
    from_email = request.POST.get('from_email', '')
    to_email = request.POST.get('to_email', '')
    email_text = "Hi " + name + "! <br><br>" + "You got a booking request from: " + \
                 from_email + " <a href = \"http://localhost:8000/" + username + "\"> (Profile) </a>" + " for your listing: '" + title + "'<br><br> Message: <br>" + message
    email_text += "<br /><a href=\"http://localhost:8000/listing/" + listing_id + "/?accept=1&requester_email=" + from_email + "\">Approve request</a> <br />"
    email_text += "<a href=\"http://localhost:8000/listing/" + listing_id + "/?ignore\">Decline request</a> <br />"
    if subject and message and from_email:
        try:
            msg = EmailMessage(subject, email_text, project_email, [to_email])
            msg.content_subtype = "html"
            msg.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')