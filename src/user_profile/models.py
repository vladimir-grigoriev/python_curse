from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Профиль'
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=20,
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length=30,
        blank=True,
        null=True
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=30
    )
    index = models.IntegerField(
        verbose_name='Индекс',
        blank=True,
        null=True
    )
    adress = models.CharField(
        verbose_name='Адрес',
        max_length=255
    )

    def __str__(self):
        return f'Профиль {self.user.username}а'
    


# Create your models here.
