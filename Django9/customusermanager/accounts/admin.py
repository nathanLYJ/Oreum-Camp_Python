from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    사용자 관리 페이지 커스터마이징 클래스입니다.
    UserAdmin을 상속받아 기본 기능을 유지하면서 커스텀 필드를 추가합니다.
    """
    # 이 관리자 클래스가 다루는 모델을 지정합니다.
    model = CustomUser

    # 사용자 목록 페이지에 표시될 필드들을 지정합니다.
    list_display = ('email', 'username', 'is_staff', 'is_active',)

    # 사용자 목록 페이지의 우측에 표시될 필터 옵션을 지정합니다.
    list_filter = ('email', 'is_staff', 'is_active',)

    # 사용자 상세 페이지에서 필드를 그룹화하여 표시하는 방식을 정의합니다.
    fieldsets = (
        # 첫 번째 그룹: 기본 정보
        (None, {'fields': ('email', 'username', 'password')}),
        # 두 번째 그룹: 권한 정보
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        # 세 번째 그룹: 개인 정보
        ('Personal Info', {'fields': ('first_name', 'last_name', 'bio', 'birth_date')}),
    )

    # 사용자 추가 페이지에서 표시될 필드들을 정의합니다.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # 'wide' 클래스를 사용하여 필드를 넓게 표시합니다.
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    # 검색 기능에 사용될 필드를 지정합니다.
    search_fields = ('email', 'username')

    # 사용자 목록의 기본 정렬 기준을 지정합니다.
    ordering = ('email',)

# CustomUser 모델을 CustomUserAdmin 설정과 함께 관리자 사이트에 등록합니다.
admin.site.register(CustomUser, CustomUserAdmin)
