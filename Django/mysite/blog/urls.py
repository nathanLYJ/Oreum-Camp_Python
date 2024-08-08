# path('경로문자열', 뷰함수, 이름)
# '': 빈 문자열은 기본 URL (홈페이지)로 매핑됩니다.
# 'posts/': '/posts/' URL로 매핑됩니다. 즉, http://yourdomain.com/posts/와 같이 접근할 수 있습니다.
# views.post_list: views.py 파일에 있는 post_list 함수를 호출합니다.
# name='post_list': URL에 이름을 부여합니다. 이 이름을 통해서 URL을 식별할 수 있습니다.
# name은 URL 패턴의 이름을 지정하는 것으로, URL 패턴을 식별하기 위해 사용합니다.
# URL 패턴을 식별할 때 사용하는 이름으로, URL 패턴을 식별하기 위해 사용합니다.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
]