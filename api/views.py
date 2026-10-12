from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions

from .models import Genre, Book, Comment
from .serializers import GenreSerializer, BookSerializer, CommentSerializer
from .permissions import IsCommentOwner


class GenreListCreateAPIView(ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer


class GenreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    lookup_field = "pk"
    lookup_url_kwarg = "genre_id"

    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer


class BookListCreateAPIView(ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        genre_id = self.kwargs.get("genre_id")
        books = Book.objects.select_related("genre")
        if genre_id:
            books = books.filter(genre_id=genre_id)
        return books

    def get_serializer_class(self):
        return BookSerializer


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    lookup_field = "pk"
    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        return Book.objects.select_related("genre")

    def get_serializer_class(self):
        return BookSerializer


class CommentListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        book_id = self.kwargs.get("book_id")
        return Comment.objects.select_related("user", "book").filter(book_id=book_id)

    def get_serializer_class(self):
        return CommentSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get("book_id"))
        serializer.save(book=book, user=self.request.user)


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsCommentOwner]
    lookup_field = "pk"
    lookup_url_kwarg = "comment_id"

    def get_queryset(self):
        return Comment.objects.select_related("user", "book")

    def get_serializer_class(self):
        return CommentSerializer
