from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'comments', views.CommentViewSet)
router.register(r'', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]