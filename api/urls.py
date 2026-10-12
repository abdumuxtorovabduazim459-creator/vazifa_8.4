from django.urls import path

from .views import (GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView,
                    BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView,
                    CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView)


urlpatterns = [
    path('genres/', GenreListCreateAPIView.as_view()),
    path('genres/<int:genre_id>/', GenreRetrieveUpdateDestroyAPIView.as_view()),
    path('books/', BookListCreateAPIView.as_view()),
    path('books/genre/<int:genre_id>/', BookListCreateAPIView.as_view()),
    path('books/<int:book_id>/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('books/<int:book_id>/comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:comment_id>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
]
