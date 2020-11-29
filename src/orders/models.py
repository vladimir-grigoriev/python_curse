import datetime
from django.utils import timezone

from django.db import models
from django.contrib.auth import get_user_model
from products.models import Book

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='carts',
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField(
        verbose_name='Created date',
        auto_now=False,
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        verbose_name='Updated date',
        auto_now=True,
        auto_now_add=False
    )

    def total_price(self):
        price = 0
        for book_in_cart in self.books.all():
            price += book_in_cart.price * book_in_cart.quantity
        return price


class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='books_in_carts'
    )
    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1,
    )
    price = models.DecimalField(
        verbose_name='Price',
        decimal_places=2,
        max_digits=6
    )
    create_date = models.DateTimeField(
        verbose_name='Create date',
        auto_now=False,
        auto_now_add=True,
    )
    update_date = models.DateTimeField(
        verbose_name='Update date',
        auto_now=True,
        auto_now_add=False
    )

    def construct_price(self):
        self. price = self.quantity * self.book.price
        return self.price

    def __str__(self):
        return f'{self.book.name}, Cart №{self.cart.pk}'


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name='Пользователь',
        blank=True,
        null=True
    )
    STATUS_CHOICES = [
        ('var1', 'Принят в обработку'),
        ('var2', 'Обработан'),
        ('var3', 'Оплачен, формируется к отгрузке'),
        ('var4', 'Отправлен, '),
        ('var5', 'Не отвечает на звонок'),
    ]
    status = models.CharField(
        verbose_name='Статус',
        max_length=4,
        choices=STATUS_CHOICES,
        default='var1'
    )
    cart = models.OneToOneField(
        Cart,
        on_delete=models.PROTECT,
        related_name='order',
        verbose_name='Order',
    )
    fio = models.CharField(
        verbose_name='ФИО',
        max_length=255,
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=20,
    )
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=40,
    )
    DELIVERY_CHOICES = [
        ('pu', 'Самовывоз'),
        ('cr', 'Доставка курьером'),
        ('pt', 'Доставка почтой')
    ]
    delivery = models.CharField(
        verbose_name='Доставка',
        max_length=2,
        choices=DELIVERY_CHOICES,
        default='pu'
    )
    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now=False,
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True,
        auto_now_add=False,
    )
    already_paid = models.BooleanField(
        verbose_name='Оплачен',
        default=False
    )

    class Meta:
        ordering = ['-create_date']