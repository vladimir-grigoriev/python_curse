from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор статьи'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )
    body = models.TextField(
        verbose_name='Статья'
    )
    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Изменено',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return self.title
    
