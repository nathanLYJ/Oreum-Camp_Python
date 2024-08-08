from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'category']
		weight = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control'}),
			'category': forms.Select(attrs={'class': 'form-control'})
		}