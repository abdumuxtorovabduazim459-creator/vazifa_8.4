from rest_framework import permissions

from rest_framework.viewsets import ModelViewSet

from .models import Book, Comment
from .serializers import BookSerializer, CommentSerializer
from .permissions import IsCommentOwnerOrReadOnly


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('-pk')
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.AllowAny,
        permissions.DjangoModelPermissions,
        IsCommentOwnerOrReadOnly,
    ]

    def get_queryset(self):
        book_id = self.request.query_params.get("book")
        if book_id:
            return self.queryset.filter(book_id=book_id)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
