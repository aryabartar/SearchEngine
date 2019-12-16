from django.urls import path

from . import views

app_name = "search"

urlpatterns = [
    path('search/', views.search, name="search"),
    path('post/<int:post_id>', views.post, name="post"),
]
