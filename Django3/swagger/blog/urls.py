from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
	path("a/", views.a, name="a"),
	path("b/", views.b, name="b"),
	path("c/", views.c, name="c"),
	path("d/", views.d, name="d"),
]