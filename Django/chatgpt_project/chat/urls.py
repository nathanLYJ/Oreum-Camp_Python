from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # 홈 URL
    path('chat/', views.ChatView.as_view(), name='chat'),  # 채팅 URL
	path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),  # 로그인 페이지
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # 로그아웃 후 홈으로 리디렉션
	
]
