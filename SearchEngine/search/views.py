from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import SearchForm
from SearchEngine.settings import *


def search(request):
    # settings.get_input1('"اشیای تاریخی فرهنگی" قاچاق')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # user_input = form.cleaned_data['user_input']
            # print(user_input)
            get_input('"اشیای تاریخی فرهنگی" !قاچاق')
            return render(request, 'search_result.html' ,  )
    else:
        form = SearchForm()
        context = {
            'form': form,
        }
        return render(request, 'index.html', context)


    # get_input('! "اشیای تاریخی فرهنگی"')
