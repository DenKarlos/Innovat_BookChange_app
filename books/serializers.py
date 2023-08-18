from rest_framework import serializers
from .models import Book, Genre
from users.models import User


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(),
                                         default=serializers.CurrentUserDefault())
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    genre = serializers.SlugRelatedField(slug_field='genre_name', queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Book
        fields = '__all__'
