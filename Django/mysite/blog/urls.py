# path('경로문자열', 뷰함수, 이름)
# '': 빈 문자열은 기본 URL (홈페이지)로 매핑됩니다.
# 'posts/': '/posts/' URL로 매핑됩니다. 즉, http://yourdomain.com/posts/와 같이 접근할 수 있습니다.
# views.post_list: views.py 파일에 있는 post_list 함수를 호출합니다.
# name='post_list': URL에 이름을 부여합니다. 이 이름을 통해서 URL을 식별할 수 있습니다.
# name은 URL 패턴의 이름을 지정하는 것으로, URL 패턴을 식별하기 위해 사용합니다.
# URL 패턴을 식별할 때 사용하는 이름으로, URL 패턴을 식별하기 위해 사용합니다.

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	# 블로그 홈페이지	 
    path('', views.home, name='home'),   	 	
	# 포스트 목록 페이지 
    path('posts/', views.post_list, name='post_list'), 
	# 포스트 상세 페이지
	path('post/<int:pk>/', views.post_detail, name='post_detail'), 
	# 포스트 작성 페이지
	path('post/new/', views.post_create, name='post_create'), 
	# 포스트 수정 페이지
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), 
	# 포스트 삭제 페이지
	path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

	# 로그인
	path('accounts/login/', auth_views.LoginView.as_view(), name='login'), 
	# 로그아웃
	path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]