from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, RentalInfoView, BookRentalView
from django.views.generic import TemplateView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('new/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('rental-info/', RentalInfoView.as_view(), name='rental_info'),
	path('rental/', BookRentalView.as_view(), name='book_rental'),
	path('rental/success/', TemplateView.as_view(template_name='books/book_success.html'), name='rental_success'),
	
]
