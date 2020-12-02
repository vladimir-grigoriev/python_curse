from django.db import models
from django.contrib.auth import get_user_model
from products.models import Book


User = get_user_model()

class Comment(models.Model):
    product = models.ForeignKey(
        Book,
        on_delete = models.CASCADE,
        related_name='comments',
        verbose_name='Товар'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Пользователь'
    )
    comment = models.TextField(
        verbose_name='Комментарий',
    )
    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now=False,
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name='Дата последнего изменения',
        auto_now=True,
        auto_now_add=False
    )