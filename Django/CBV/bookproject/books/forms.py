from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'genre', 'summary', 'image']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),  # 날짜 선택기를 위한 위젯 설정
        }
        labels = {
            'title': '제목',
            'author': '저자',
            'publication_date': '출판일',
            'genre' : '장르',
            'summary' : "요약",
            'image' : "이미지"
        }
