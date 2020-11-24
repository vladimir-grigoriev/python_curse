from django.contrib import admin
from .models import Cart, BookInCart, Order
# Register your models here.

admin.site.register(Cart)
admin.site.register(BookInCart)
admin.site.register(Order)