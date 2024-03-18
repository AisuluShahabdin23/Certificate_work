from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """ Отображение пользователей """
    # Username = None, так как мы будем использовать поле "email"
    username = None

    email = models.EmailField(unique=True, verbose_name='Электронная почта пользователя')
    phone = models.CharField(max_length=30, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=55, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=55, verbose_name='Город', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активен')

    # Поле "email" будет использоваться для идентификации пользователя
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
