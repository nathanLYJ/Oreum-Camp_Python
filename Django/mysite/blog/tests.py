from django.test import TestCase
from blog.models import Post, Category
from django.utils import timezone  

# Create your tests here.
category = Category.objects.create(name = "Python", description = "Python에 대한 모든것")
post = Post.objects.create(title="두 번째 블 로 그", content="나의 두 번 째  블 로 그 에 요", category = category)
print(post)