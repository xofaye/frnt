import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from jsonview.decorators import json_view

from .services import furniture_search


class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def home(request):
    context = {}
    return render(request, 'index.html', context)

@login_required
@json_view
def search_furniture(request):
    logging.warning(request.GET.get('q'))
    return furniture_search(request.GET['q'])