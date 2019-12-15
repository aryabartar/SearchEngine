from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from django.conf import settings
from .forms import SearchForm


def search(request):
    # settings.get_input1('"اشیای تاریخی فرهنگی" قاچاق')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['user_input'])

    else:
        form = SearchForm()

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)
