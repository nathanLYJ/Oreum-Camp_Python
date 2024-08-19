from django.urls import path, include


# Function Based URL
# from .views import movie_list
# urlpatterns = [
#     path('movies/', movie_list, name='movie-list'),
# ]

# Class Based URL
# from .views import MovieListAPIView, MovieDetailAPIView


from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    # path('movies/', MovieListAPIView.as_view(), name='movie-list'),
    # path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),  # 영화 세부 정보 조회, 수정, 삭제
	path('', include(router.urls)),
	
]