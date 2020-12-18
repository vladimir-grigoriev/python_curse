from django.apps import AppConfig
from django.db.models.signals import pre_save, post_delete

class ProductsConfig(AppConfig):
    name = 'products'
    verbose_name = 'Справочники'

    def ready(self):
        from .models import Book
        from .signals import image_cleaner

        post_delete.connect(image_cleaner, sender=Book)
