import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from jsonview.decorators import json_view

from .services import furniture_search
from .forms import SignUpForm


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
    logging.warning(request.GET.get('q'))
    return furniture_search(request.GET['q'])