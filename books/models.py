from django.db import models
from users.models import User

class BaseModel(models.Model):
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    deleted_date = models.DateTimeField(verbose_name="Дата удаления", null=True, blank=True)

    class Meta:
        abstract = True

class Book(BaseModel):
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
        ordering = ['title']

    def __str__(self):
        return f'Книга: {self.title}'


class Genre(BaseModel):
    genre_name = models.CharField(max_length=100, verbose_name='название жанра', unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'Жанр: {self.genre_name}'
    

class Order(BaseModel):
    
    STATUS_CHOICES = (
        ('ОП', 'Ожидание подтверждения'),
        ('ЗП', 'Запрос принят'),
        ('ДОС', 'Детали обмена согласованы'),
        ('ОЗ', 'Обмен завершён'),
        ('Откл', 'Отклонён'),
        ('Отм', 'Отменён'),
    )

    requester = models.ForeignKey(Book, verbose_name="Получаемая Книга", on_delete=models.CASCADE,related_name='requested')
    requested_part = models.ForeignKey(Book, verbose_name="Выдаваемая Книга", on_delete=models.CASCADE,related_name='requested_parts')
    status = models.CharField(max_length=100, choices = STATUS_CHOICES, default='ОП', null=False)
    
    requester_approval = models.BooleanField("Одобрить Получение")
    requested_part_approval = models.BooleanField("Одобрить Выдачу")
    requester_is_changed = models.BooleanField("Получение Изменен")
    requested_part_is_changed = models.BooleanField("Выдача Изменен")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'

    def __str__(self):
        return f'{self.requester} на {self.requested_part}'
    

class Chat(BaseModel):
    
    messege = models.CharField(max_length=500, verbose_name='Сообщение', null=False)
    owner_user = models.ForeignKey(User, verbose_name="Отправитель сообщения", on_delete=models.CASCADE)
    owner_book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чат'

    def __str__(self):
        return f'Сообщение: {self.messege}'