from book import views

from django.urls import path


app_name = 'book'

urlpatterns = [
    path('authors/', views.AuthorsView.as_view(), name='authors'),
    path('authors/<int:pk>/', views.AuthorView.as_view(), name='author'),

    path('books/', views.BooksView.as_view(), name='books'),
    path('books/<int:pk>/', views.BookView.as_view(), name='book'),
]
