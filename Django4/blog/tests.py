from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from blog.models import Post
from notice.models import PostNotice


class PostTest(TestCase):
    """
    Blog앱 Post 모델 테스트와 Notice앱 PostNotice 모델 테스트

    blog > tests에는 Post 모델 테스트만 해야 합니다.
    notice > tests에는 PostNotice 모델 테스트만 해야 합니다.

    수업에서만 사용할 테스트 코드입니다.
    """

    def setUp(self):
        """
        테스트에 사용할 데이터 생성
        """
        print("--main app 세팅 시작--")
        # 어차피 실제 서비스에서는 사용하지 않는 코드이기 때문에 부하가 되더라도 출력을 해서 어느 단에서 멈추는지 확인
        self.client = APIClient()
        # 주의 사항! 테스트 코드가 유출되는 경우도 종종 발생됩니다. 따라서 테스트 코드를 작성할 때는 중요한 정보를 넣지 않도록 주의해야 합니다.
        self.user = User.objects.create_user(
            username="hojunjun", password="dlghwns1234!"
        )
        self.user.save()
        self.notice = PostNotice.objects.create(
            title="notice title", content="notice content", author=self.user
        )
        self.notice.save()
        self.post = Post.objects.create(
            title="post title", content="post content", author=self.user
        )
        self.post.save()
        print("--// main app 세팅 끝--")

    def test_notice_read(self):
        """
        함수명은 test_get_notice_list_anonymous,
        test_post_notice_authenticated와 같은 식으로
        `test_메서드_앱_기능_상태`로 작성하면 좋습니다.

        지금은 함수 이름이 간소화 되어 있습니다.

        회원이 아닌 사람이 notice를 읽으려 할 때
        notice Read 가능 테스트
        """
        print("-- notice read 시작 --")
        response = self.client.get("/notice/")
        self.assertEqual(response.status_code, 200)
        # response에 데이터 출력
        print(response.data)
        print("--// notice read 끝--")

    def test_notice_CUD(self):
        """
        회원이 notice를 작성할 때
        notice Create 가능 테스트

        가능하면 create, update, delete를 별도로 테스트하는 것이 좋습니다.
        """
        print("-- notice create 시작 --")
        self.client.login(username="hojunjun", password="dlghwns1234!")
        # self.client.force_authenticate(user=self.user)
        # self.user.save()
        response = self.client.post(
            "/notice/",
            {
                "title": "notice title",
                "content": "notice content",
                "author": self.user.pk,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        # response에 데이터 출력
        print(response.data)
        print("--// notice create 끝--")

        print("-- notice update 시작 --")
        response = self.client.put(
            f"/notice/1/",
            {
                "title": "notice title",
                "content": "notice content",
                "author": self.user.pk,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        print("--// notice update 끝--")

        print("-- notice delete 시작 --")
        response = self.client.delete(f"/notice/1/")
        self.assertEqual(response.status_code, 204)
        print("--// notice delete 끝--")

    def test_notice_nonmember(self):
        """
        비회원인 사람은 notice CUD 불가능 테스트
        """
        print("-- notice 비회원 CUD 테스트 BEGIN")
        response = self.client.post(
            "/notice/",
            {"title": "test title", "content": "test content", "author": self.user.pk},
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.put(
            f"/notice/1/",
            {
                "title": "update title",
                "content": "update_content",
                "author": self.user.pk,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.delete(f"/notice/1/")
        self.assertEqual(response.status_code, 403)
        print("-- notice 비회원 CUD 테스트 END")