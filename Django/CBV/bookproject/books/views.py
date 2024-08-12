from django.views.generic import ListView, TemplateView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

# Create your views here.
class BookListView(ListView):
    model = Book # 이 뷰에서 사용할 모델
    template_name = 'books/book_list.html' # 랜더링할 템플릿 파일! 
    context_object_name = 'books' # 컨텍스트 객체 이름! 기본적으로 object_list를 사용함 books 변경
    ordering = ['-publication_date'] # 출판일 기준 내림차순으로 정렬
    paginate_by = 5 # 페이지네이션을 사용하겠다는 의미

class MainView(TemplateView):
    template_name = 'main.html' # 랜더링할 템플릿 파일

class BookDetailView(DetailView):
    model = Book # 이 뷰에서 사용할 모델
    template_name = 'books/book_detail.html' # 랜더링할 템플릿 파일
    context_object_name = 'book' # 컨텍스트 객체 이름! 기본적으로 object를 사용함 book 변경

class BookCreateView(CreateView):
    model = Book # 이 뷰에서 사용할 모델
    template_name = 'books/book_form.html' # 랜더링할 템플릿 파일
    form_class = BookForm # 사용할 폼 클래스
    success_url = reverse_lazy('books:book_list') # 성공 시 이동할 URL

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'

    def get_success_url(self):
        return reverse_lazy('books:book_detail', kwargs={'pk': self.object.pk})
    

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')


# URL패턴을 지정!
# Template를 구성해서 사용자가 접근할 수 있도록 함!
# 첫번째 화면이 구성되게 됩니다!!

# 컨텍스트 객체 이름 -> 원래는 object_list로 사용되지만, book_list로 변경