from django import forms
from .models import Task, List

class TaskForm(forms.ModelForm):
    # list 필드에 대한 ModelChoiceField를 생성
    list = forms.ModelChoiceField(queryset=List.objects.all(), empty_label=None, required=False)
    
    class Meta:
        model = Task  # task모델과 해당 폼이 연결됨
        fields = ['title', 'description', 'due_date', 'list']  # 폼에 나타날 필드들
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'datetime-local'}),  # 날짜와 시간을 입력할 수 있는 위젯
        }
