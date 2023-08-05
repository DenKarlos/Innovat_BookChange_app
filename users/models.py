from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'username']

    phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")  # by standart E.164
    phone = models.CharField(validators=[phone_regex], max_length=16, unique=True,
                             error_messages={
                                 "unique": "Пользователь с таким номером телефона уже существует",
                             },
                             verbose_name='номер телефона')
    photo = models.ImageField(upload_to='user_photo/', blank=True, verbose_name='фотография')
    email = models.EmailField(verbose_name='e-mail', unique=True,
                              error_messages={"unique": "пользователь с таким e-mail адресом уже существует"})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']

    def __str__(self):
        return f'Пользователь: {self.username}'
