from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .serializers import PostSerializer, TagSerializer
from rest_framework import status
from .models import Post, Tag


@extend_schema(
    summary="Blog list",
    description="이 블로그는 영국에서 시작되어... GET 요청에 대한 응답입니다.",
    responses={200: "Blog list response"},
)
@api_view(["GET"])
def blog_list(request):
    return Response("blog_list")


@extend_schema(
    summary="Post 생성",
    description="데이터 스키마에 따라서(데이터 스키마 설명..) POST로 데이터를 받아 저장합니다.",
    request=PostSerializer,
    responses={200: PostSerializer(many=True)},
)
@api_view(["GET", "POST"])
def a(request):
    """
    blog 데이터를 POST로 받아서 데이터베이스 저장
    """
    if request.method == "GET":
        return Response("a GET")
    else:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response("a POST")


@api_view(["GET", "POST"])
def b(request):
    if request.method == "GET":
        return Response("b GET")
    else:
        return Response("b POST")


@api_view(["GET", "PUT", "DELETE"])
def c(request):
    # 0번째 인덱스 처리
    if request.method == "GET":
        post = Post.objects.get(pk=1)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        post = Post.objects.get(pk=1)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        post = Post.objects.get(pk=1)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@extend_schema(
    summary="Post 부분 수정, Tag 전체 조회, HEAD 요청",
    description="serializer에 partial=True를 넣어서 부분 수정을 허용, HEAD 요청은 응답만을 반환, GET 요청은 모든 태그를 반환.",
    request=PostSerializer,
    responses={200: PostSerializer()},
)

@api_view(["PATCH","HEAD", "GET"])
def d(request):
    if request.method == "PATCH":
        post = Post.objects.get(pk=1)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "HEAD":
        return Response(status=status.HTTP_200_OK)
    elif request.method == "GET":
        # GET 요청을 처리하여 모든 태그를 반환합니다.
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


        