from django.shortcuts import render
from .models import Person, User, Post, Like
from django.http import HttpResponse


def person_list(request):
	# 데이터 추가 코드
    # user = User.objects.get(username='nathan')
    # new_post = Post(title='title2', contents='contents2', category='category2', user=user)
    # new_post.save()
    # return HttpResponse('데이터 추가 완료')
	
    # 데이터 조회 코드
    # post = Post.objects.all()
    # html = "<h1>Post List</h1><ul>"
    # for p in post:
    #     html += f"<li>{p.title} {p.contents} {p.like}</li>"
    # html += "</ul>"
    # return HttpResponse(html)
	
    # 데이터 수정 코드
    # post = Post.objects.get(id=1)
    # post.title = 'sql 어려워요...  '
    # post.contents = 'sql 너무 어려워요...  '
    # post.save()
    # return HttpResponse('데이터 수정 완료')
	
    # 데이터 삭제 코드
    # post = Post.objects.get(id=1)
    # post.delete()
    # return HttpResponse('데이터 삭제 완료')
	
    # 좋아요 기능 코드
    # user = User.objects.get(username='nathan')
    # post = Post.objects.get(id=2)
    # new_like = Like(post=post, user=user)
    # new_like.save()
    # return HttpResponse('좋아요 완료')
	
    def some_view(request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user  # Assuming the user is logged in
        has_liked = post.is_liked_by_user(user)
        
        if has_liked:
            # User has liked the post
            print("User has liked this post.")
        else:
            # User has not liked the post
            print("User has not liked this post.")