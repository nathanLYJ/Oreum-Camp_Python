# 이 부분은 Rest_framework의 기본 뼈대를 만드는 부분 -> 이 클래스를 상속받아서 HTTP 메서드(Get, Post, Put, Delete)를 구현할 수 있다.
from rest_framework.views import APIView
# API 뷰에서 반환하는 응답객체 -> 딕셔너리를 -> JSON으로 변환하여 반환한다. 
# 클라이언트에게 전달할 메세지를 정해진 양식 (표준화된 API 형식)에 따라 데이터 전달하는 방법
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

# ViewSet을 상속받아서 CRUD를 구현할 수 있다.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



# Function Based View
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         # many=True : 여러개의 데이터를 직렬화할 때 사용 -> 여러개의 영화 데이터를 한번에 JSON으로 변환
#         serializer = MovieSerializer(movies, many=True)
#         # 직렬화된 데이터를 JSON 형식으로 반환
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         # 클라이언트로부터 전달된 데이터를 기반으로 MovieSerializer 객체를 생성 -> 새로운 영화 데이터를 준비!
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_vaild():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Class Based View
# class MovieListAPIView(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MovieDetailAPIView(APIView):
#     def get_object(self, pk):
#         # Movie 객체를 가져오거나 404 에러를 반환하는 유틸리티 사용
#         return get_object_or_404(Movie, pk=pk)

#     def get(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
