import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from jsonview.decorators import json_view
from django.core import serializers

from .services import furniture_search
from .forms import SignUpForm, SearchFurnitureForm, EditProfileForm, LocationForm, AddListingForm, EditListingForm
from .models import Listing, Location, Profile


class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def home(request):
    args = {}
    args['search_form'] = SearchFurnitureForm()

    return render(request, 'index.html', args)


def dashboard(request):
    listings = Listing.objects.all()[:5]
    context = {'listings': listings}
    return render(request, 'dashboard.html', context)


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

@login_required
@json_view
def search_furniture(request):
    response = {}
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
            query_set2 = serializers.serialize('json', query_set)

            return render(request, 'listings.html', {'data': query_set})

    args = {}
    args['form'] = SearchFurnitureForm()
    return render(request, 'search.html', args)

@login_required
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

    context = {'user': request.user, 'profile': profile}
    return render(request, 'view_profile.html', context)


def view_listing(request, id):
    listing = get_object_or_404(Listing, id__iexact=id)

    context = {'user': request.user, 'listing': listing}
    return render(request, 'view_listing.html', context)

def add_listing(request):
    loc_form = LocationForm(request.POST or None)
    form = AddListingForm(request.POST or None)

    if request.method == 'POST':
        if loc_form.is_valid():
            street_address = loc_form.cleaned_data['street_address']
            city = loc_form.cleaned_data['city']
            postal_code = loc_form.cleaned_data['postal_code']
            country = loc_form.cleaned_data['country']

            l = None
            if street_address or city or postal_code or country:
                l = Location.objects.create(street_address=street_address, city=city,
                                        postal_code=postal_code, country=country)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                picture = form.cleaned_data['picture']
                price = form.cleaned_data['price']
                listing = Listing.objects.create(title=title, description=description, 
                    picture=picture, price=price, location=l, user=request.user.profile)
            return redirect('dashboard')

    context = {
        'form': form,
        'loc_form': loc_form,
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