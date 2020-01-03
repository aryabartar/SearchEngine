from django.urls import path

from . import views

app_name = "search"

urlpatterns = [
    path('', views.search, name="search"),
    path('posts/<int:post_id>', views.post, name="post"),
]
