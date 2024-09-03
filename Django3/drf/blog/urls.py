from django.urls import path
from .views import blog_list, csrf

urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("csrf/", csrf, name="csrf"),
]