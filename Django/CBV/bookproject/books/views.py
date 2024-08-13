from django.views.generic import ListView, TemplateView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm, CustomUserCreationForm, RentalForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .mixins import GroupRequiredMixin
from django.views.generic import TemplateView



# Create your views here.
class BookListView(ListView):
    model = Book # 이 뷰에서 사용할 모델
    template_name = 'books/book_list.html' # 랜더링할 템플릿 파일! 
    context_object_name = 'books' # 컨텍스트 객체 이름! 기본적으로 object_list를 사용함 books 변경
    ordering = ['-publication_date'] # 출판일 기준 내림차순으로 정렬
    paginate_by = 5 # 페이지네이션을 사용하겠다는 의미

    def get_queryset(self):
        queryset = super().get_queryset() 
        
        query = self.request.GET.get('q') # q라는 파라미터로 전달된 값 가져오기 q는 query의 약자
        if query:
        # title, author, genre 모두에서 검색되도록 Q 객체를 사용하여 OR 조건 추가
            queryset = queryset.filter(
            Q(title__icontains=query) | 
            Q(author__icontains=query) | 
            Q(genre__icontains=query)
        )
        
        # 정렬조건에 대해서 처리
        sort = self.request.GET.get('sort')
        if sort == 'title':
            queryset = queryset.order_by('title')
        elif sort == 'author':
            queryset = queryset.order_by('author')
        elif sort == 'publication_date':
            queryset = queryset.order_by('publication_date')
        else:
            queryset = queryset.order_by('-publication_date')
        # 필터링 처리   
        genre = self.request.GET.get('genre')
        if genre:
            queryset = queryset.filter(genre=genre)

        return queryset
        

class MainView(TemplateView):
    template_name = 'main.html' # 랜더링할 템플릿 파일

class BookDetailView(DetailView):
    model = Book # 이 뷰에서 사용할 모델
    template_name = 'books/book_detail.html' # 랜더링할 템플릿 파일
    context_object_name = 'book' # 컨텍스트 객체 이름! 기본적으로 object를 사용함 book 변경

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book # 이 뷰에서 사용할 모델
    template_name = 'books/book_form.html' # 랜더링할 템플릿 파일
    form_class = BookForm # 사용할 폼 클래스
    success_url = reverse_lazy('books:book_list') # 성공 시 이동할 URL

class BookUpdateView(GroupRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:book_detail')
    group_name = 'Editor'

    def get_success_url(self):
        return reverse_lazy('books:book_detail', kwargs={'pk': self.object.pk})
    

class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')
    permission_required = 'books.delete_book' # 권한 설정


# URL패턴을 지정!
# Template를 구성해서 사용자가 접근할 수 있도록 함!
# 첫번째 화면이 구성되게 됩니다!!

# 컨텍스트 객체 이름 -> 원래는 object_list로 사용되지만, book_list로 변경

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login') # 성공시 이동할 페이지



class RentalInfoView(TemplateView):
    template_name = 'books/rental_info.html'

class BookRentalView(LoginRequiredMixin, FormView):
    template_name = 'books/book_rental.html'
    form_class = RentalForm
    success_url = reverse_lazy('books:rental_success')  # 네임스페이스와 함께 사용

    def form_valid(self, form):
        rental = form.save(commit=False)
        rental.user = self.request.user  # 로그인된 사용자를 할당
        rental.save()
        return super().form_valid(form)