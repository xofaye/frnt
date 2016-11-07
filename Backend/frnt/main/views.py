import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from jsonview.decorators import json_view

from .services import furniture_search
from .forms import SignUpForm, SearchFurnitureForm
from .models import FnrtListing


class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def home(request):
    context = {}
    return render(request, 'index.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


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
    if request.method == 'POST':
        form = SearchFurnitureForm(request.POST)
        if form.is_valid():
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']
            location = form.cleaned_data['location']
            results = FnrtListing.objects.raw('SELECT * FROM FnrtListing '
                                              'WHERE price >= %s AND price <= %s AND location == %s',
                                              min_price, max_price, location)

            return results
    logging.warning(request.GET.get('q'))
    return furniture_search(request.GET['q'])