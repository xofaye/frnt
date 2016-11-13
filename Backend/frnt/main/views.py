import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from jsonview.decorators import json_view
from django.core import serializers

from .services import furniture_search
from .forms import SignUpForm, SearchFurnitureForm, EditProfileForm, LocationForm
from .models import Listing, Location


class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def home(request):
    context = {}
    return render(request, 'index.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


def logout_success(request):
    logout(request)
    return render(request, 'logout_success.html')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return redirect('home')
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
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']
            location = form.cleaned_data['location']

            query_set = Listing.objects.filter(price__gte=min_price, price__lte=max_price,
                                               location__city__contains=location, location__country__contains=location)
            query_set2 = serializers.serialize('json', query_set)
            print (query_set2)

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


def view_profile(request):
    context = {'user': request.user.user}
    return render(request, 'main/view_profile.html', context)
