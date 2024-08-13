from django import forms
from .models import Book, Rental
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class CustomUserCreationForm(UserCreationForm):
    # 현재 원하는 필드가 모델에 없기 때문에 직접 추가
    email = forms.EmailField(label='이메일', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
                  
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['book', 'return_date']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }