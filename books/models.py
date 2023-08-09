from django.db import models
from users.models import User


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='название книги', db_index=True)
    authors = models.CharField(max_length=200, verbose_name='авторы', null=True, blank=True)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    language = models.CharField(max_length=100, verbose_name='язык', null=True, blank=True)
    publication_year = models.IntegerField(verbose_name='год публикации', null=True, blank=True)
    genre = models.ManyToManyField(to='Genre', related_name='books', blank=True,)
    time_create = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='время обновления', auto_now=True)
    owner = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE)
    is_ordered = models.BooleanField(verbose_name='участие в запросе', default=False)
    photo = models.ImageField(upload_to='book_photo/', blank=True, verbose_name='фотография книги')


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-time_create']

    def __str__(self):
        return f'Книга: {self.title}'


class Genre(models.Model):
    genre_name = models.CharField(max_length=100, verbose_name='название жанра', unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['genre_name']

    def __str__(self):
        return f'Жанр: {self.genre_name}'
