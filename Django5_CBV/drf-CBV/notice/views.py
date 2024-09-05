from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import PostNotice
from .serializers import PostSerializer
from django.http import Http404


class NoticeList(APIView):
	permission_classes = [IsAuthenticatedOrReadOnly]

	def get(self, request):
		posts = PostNotice.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(author=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoticeDetail(APIView):
	permission_classes = [IsAuthenticatedOrReadOnly]

	def get_object(self, pk):
		try:
			return PostNotice.objects.get(pk=pk)
		except PostNotice.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		post = self.get_object(pk)
		serializer = PostSerializer(post)
		return Response(serializer.data)

	def put(self, request, pk):
		post = self.get_object(pk)
		if post.author != request.user:
			return Response(status=status.HTTP_403_FORBIDDEN)
		serializer = PostSerializer(post, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		post = self.get_object(pk)
		if post.author != request.user:
			return Response(status=status.HTTP_403_FORBIDDEN)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


notice_list = NoticeList.as_view()  # urls.py를 수정하지 않기 위해 추가
notice_detail = NoticeDetail.as_view()  # urls.py를 수정하지 않기 위해 추가