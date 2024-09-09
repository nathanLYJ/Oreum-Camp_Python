from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    커스텀 유저 모델을 위한 매니저 클래스입니다.
    이 클래스는 새 사용자를 생성하는 메서드를 제공합니다.
    """
    def create_user(self, email, username, password=None, **extra_fields):
        """
        일반 사용자를 생성하는 메서드입니다.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)  # 이메일 정규화
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)  # 비밀번호 해싱
        user.save(using=self._db)  # 사용자를 데이터베이스에 저장
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        관리자(superuser) 사용자를 생성하는 메서드입니다.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # 관리자는 반드시 is_staff와 is_superuser가 True여야 합니다.
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    커스텀 유저 모델 클래스입니다.
    AbstractBaseUser를 상속받아 기본 인증 기능을 제공받고,
    PermissionsMixin을 상속받아 Django의 권한 시스템을 사용합니다.
    """
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)  # 관리자 사이트 접근 권한
    is_active = models.BooleanField(default=True)  # 계정 활성화 상태
    date_joined = models.DateTimeField(default=timezone.now)  # 가입 일자
    bio = models.TextField(max_length=500, blank=True)  # 자기소개
    birth_date = models.DateField(null=True, blank=True)  # 생년월일

    objects = CustomUserManager()  # 커스텀 매니저 지정

    homepage_url = models.URLField(blank=True,null=True)  # 홈페이지 주소

    USERNAME_FIELD = 'email'  # 로그인에 사용할 필드 지정
    REQUIRED_FIELDS = ['username']  # createsuperuser 명령어 실행 시 요구되는 필드

    class Meta:
        """
        관리자 페이지 등에서 보여질 단수이름, 복수이름을 지정합니다.
        """
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email  # 객체를 문자열로 표현할 때 이메일 반환
    
    def save(self, *args, **kwargs):
        # 슈퍼유저와 일반 유저 모두에 대해 homepage_url을 자동 생성하는 로직
        if not self.homepage_url:
            self.homepage_url = f"http://127.0.0.1:8000/users/{self.username}"
        super().save(*args, **kwargs)