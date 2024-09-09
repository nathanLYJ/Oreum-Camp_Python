from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModerSerializer):
	class Meta:
		model = Post
		fields = ['id', 'title', 'content']