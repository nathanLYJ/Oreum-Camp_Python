from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'publication_date', 'genre'] # 목록에 보여줄 필드
	search_fields = ['title', 'author'] # 검색 기능 추가
	list_filter = ['publication_date'] # 필터 기능 추가
	ordering = ('-publication_date',)  # 출판일을 기준으로 내림차순 정렬
