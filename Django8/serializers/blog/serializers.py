# from rest_framework import serializers
# from .models import Post


# class PostSerializer(serializers.ModelSerializer):
#     author_username = serializers.SerializerMethodField()
#     testdata = serializers.SerializerMethodField()
#     testdata2 = serializers.SerializerMethodField()
#     testdata3 = serializers.SerializerMethodField()

#     # 모델에는 없는 필드를 만드는 방법은 명시적인 방법과 암시적인 방법이 있습니다.
#     # 위 방법은 명시적인 방법입니다.
#     # 이러한 방식을 사용했을 때에는 여러 파리터를 사용할 수 있습니다.

#     class Meta:
#         model = Post
#         fields = [
#             "id",
#             "author",
#             "caption",
#             "created_at",
#             "author_username",
#             "testdata",
#             "testdata2",
#             "testdata3",
#         ]

#     def get_author_username(self, obj):
#         return obj.author.username

#     def get_testdata(self, obj):
#         return "test!!"

#     def get_testdata2(self, obj):
#         # obj가 Post가 맞는지 확인하는 작업일 뿐입니다.
#         value = f"<--{obj.caption}-->"
#         return value

#     def get_testdata3(self, obj):
#         return len(obj.caption)

from rest_framework import serializers
from .models import Comment, Post, Like

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'text', 'created_at']
        read_only_fields = ['author']

    def get_author_username(self, obj):
        # 이 메소드는 'author_username' 필드의 값을 생성합니다.
        # obj는 현재 처리 중인 Comment 인스턴스입니다.
        # 필드 이름이 'author_username'이면 'get_필드명' 형식의 메소드를 호출하여 값을 생성합니다.
        # 이 필드는 실제 Comment 모델에는 없지만, 이 필드를 통해 댓글 작성자의 사용자 이름을 반환합니다.
        return obj.author.username  # 댓글 작성자의 사용자 이름을 반환합니다.

    def create(self, validated_data):
        # 시리얼라이저에서 .save() 메소드를 호출할 때 실행됩니다.
        # 댓글 생성 시 현재 인증된 사용자를 작성자로 설정합니다.
        # self.context['request']를 통해 현재 요청 객체에 접근할 수 있습니다.
        validated_data['author'] = self.context['request'].user
        # 부모 클래스의 create 메소드를 호출하여 댓글을 생성합니다.
        return super().create(validated_data)

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField() # 명시적 방법입니다. 없으면 암시적으로 작동합니다. 명시적으로 작성할 경우 파라미터 값을 지정할 수 있습니다.
    comments = CommentSerializer(many=True, read_only=True)
    likesCount = serializers.IntegerField(source='likes.count', read_only=True)
    isLiked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'caption', 'created_at', 'comments', 'likesCount', 'isLiked']
        read_only_fields = ['author']

    def get_isLiked(self, obj):
        # 현재 사용자가 이 게시물에 좋아요를 눌렀는지 확인합니다.
        user = self.context['request'].user
        if user.is_authenticated:
            # Like 모델을 사용하여 현재 사용자가 게시물에 좋아요를 눌렀는지 확인합니다.
            return Like.objects.filter(post=obj, user=user).exists()
        return False
    
    def get_author_username(self, obj):
        # 게시물 작성자의 사용자 이름을 반환합니다.
        return obj.author.username

    def create(self, validated_data):
        # 게시물 생성 시 현재 인증된 사용자를 작성자로 설정합니다.
        validated_data['author'] = self.context['request'].user
        print(validated_data['author'])
        print(validated_data)
        print(self.context['request'])
        return super().create(validated_data)