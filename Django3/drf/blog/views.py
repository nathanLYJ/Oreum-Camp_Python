from django.shortcuts import render
from .models import Post
from django.http import JsonResponse, HttpResponse
# DRF 추가 후 추가된 코드
from rest_framework import views, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# 시리얼라이저 추가	
from .serializers import PostSerializer
# CSRF 토큰 추가
from django.middleware.csrf import get_token

# #DRF 테스트 코드
# # step1: 가벼운 응답
# def blog_list(request):
# 	return JsonResponse("blog_list")

# # step2: object를 하나씩 객체로 만들어서 응답
# def blog_list(request):
# 	posts = Post.objects.all()
# 	post_list = []
# 	for post in posts:
# 		post_list.append({
# 			"title": post.title,
# 			"content": post.content,
# 		})
# 	return HttpResponse(post_list)

# # step3: object를 하나씩 객체로 만들어서 json으로 응답
# def blog_list(request):
#     posts = Post.objects.all()
#     post_list = []
#     for post in posts:
#         post_list.append(
#             {
#                 "title": post.title,
#                 "content": post.content,
#             }
#         )
#     # safe=False: list를 json으로 변환할 수 있도록 허용(dict가 아닌경우 False로 설정)
#     return JsonResponse(post_list, safe=False)

# # step4: 이렇게 굳이 하나씩 뜯어서 json으로 변환할 필요 없이, values()를 사용하면 한번에 json으로 변환 가능
# def blog_list(request):
#     posts = Post.objects.all()
#     post_list = list(posts.values())  # 주석처리 해보고 전달 해보세요.
#     return JsonResponse(post_list, safe=False)

# # FBV 방식 rest_framework를 사용한 코드
# @api_view(["GET"])  # get 요청으로 들어오는 코드를 처리해주겠다!
# def blog_list(request):
#     posts = [
#         {"title": "1", "content": "111"},
#         {"title": "2", "content": "222"},
#         {"title": "3", "content": "333"},
#         {"title": "4", "content": "444"},
#     ]
#     serializer = (
#         posts  # 직렬화 하는 단계(이 단계는 지금은 필요 없으나, 나중에 필요합니다.)
#     )
#     return Response(serializer)  # 직렬화한 데이터를 Response로 반환

# # CBV 방식 rest_framework를 사용한 코드
# class BlogList(APIView):
# 	def get(self, request):
# 		posts = [
# 			{"title": "1", "content": "111"},
# 			{"title": "2", "content": "222"},
# 			{"title": "3", "content": "333"},
# 			{"title": "4", "content": "444"},
# 		]
# 		serializer = (
# 			posts  # 직렬화 하는 단계(이 단계는 지금은 필요 없으나, 나중에 필요합니다.)
# 		)
# 		return Response(serializer)  # 직렬화한 데이터를 Response로 반환

# blog_list = BlogList.as_view()

# # rest_framework를 작성후, serializer 테스트 코드
# @api_view(["GET"])  # get 요청으로 들어오는 코드를 처리해주겠다!
# def blog_list(request):
#     posts = Post.objects.all()
#     # 다수의 데이터를 넣을 때에는 many를 활성화 하셔야 합니다.
#     serializer = PostSerializer(posts, many=True)
#   # print(type(serializer))  # <class 'rest_framework.serializers.ListSerializer'>
#   # print(dir(serializer))
#   # print(serializer.data)  # 리스트의 형태로 보입니다.
#   # print(
#   #     type(serializer.data)
#   # )  # <class 'rest_framework.utils.serializer_helpers.ReturnList'>
#     return Response(serializer.data)  # 직렬화한 데이터를 Response로 반환

# rest_framework를 작성후, serializer 테스트 코드
@api_view(["GET", "POST"])
def blog_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)  # 직렬화한 데이터를 Response로 반환


def csrf(request):
    token = get_token(request)
    return JsonResponse({"csrftoken": token})

