from django.urls import path
from .views import notice_list, notice_detail

app_name = "notice"
# notice 앱의 url 설정
urlpatterns = [
	path("notice/", notice_list),
	path("notice/<int:pk>/", notice_detail),
]
