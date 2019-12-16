from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import SearchForm
from SearchEngine.settings import *


def post(request, post_id):
    post = posts_list[post_id - 1]
    context = {
        "id": post.id,
        "publish_date": post.publish_date,
        "title": post.title,
        "url": post.url,
        "summary": post.summary,
        "meta_tags": post.meta_tags,
        "content": post.content,
        "thumbnail": post.thumbnail,
    }

    return render(request, 'post-page.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            print(user_input)
            # result_list = get_input('"اشیای تاریخی فرهنگی" !قاچاق')

            return render(request, 'search-result.html', {"result_list": result_list})
    else:
        form = SearchForm()
        context = {
            'form': form,
        }
        return render(request, 'index.html', context)
