from rest_framework import serializers

from .models import Genre, Book, Comment

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = []
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'min_length': 2},
            'description': {'required': False},
        }


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = []
        read_only_fields = ['id']
        extra_kwargs = {
            'pages': {'min_value': 1},
        }


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'book', 'user', 'text', 'created_at']
        read_only_fields = ['id', 'book', 'user', 'created_at']
