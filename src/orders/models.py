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

    def total_price(self):
        price = 0
        for book_in_cart in self.books.all():
            price += book_in_cart.price
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

    def construct_price(self):
        price = self.quantity * self.book.price
        return price

    def __str__(self):
        return f'{self.book.name} for { self.cart.customer.username }'