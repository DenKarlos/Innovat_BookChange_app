from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='название книги', db_index=True)
    authors = models.CharField(max_length=200, verbose_name='авторы', null=True,  blank=True )
    publication_year = models.IntegerField(verbose_name='год публикации', null=True,  blank=True)
    genre = models.ManyToManyField(to='Genre', related_name='books', null=True,  blank=True)
    created = models.DateTimeField(verbose_name='время добавления', auto_now_add=True, )