from django.db import models
from directory.models import Author, Genre, Series, Publisher, Binding, BookFormat, AgeRestriction


class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=255,
        default='Без названия',
        help_text='Введите название книги'
    )
    foto = models.ImageField(
        verbose_name='Фото обложки',    
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=6,
        decimal_places=2,
        help_text='Цена в белорусских рублях'
    )
    author = models.ManyToManyField(
        Author,
        related_name='author',
        verbose_name='ФИО автора',
        max_length=100,
        default='Автор неизвестен',        
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        related_name='series',
        verbose_name='Серия книг',
    )
    genres = models.ManyToManyField(
        Genre,
        related_name='genres',
        verbose_name='Жанр книги',
        max_length=50,
        default='Жанр не указан',
    )
    year_published = models.IntegerField(
        verbose_name='Год публикации',
        null=True,
        blank=True,
    )
    nubmer_of_pages = models.IntegerField(
        verbose_name='Количество страниц',
        null=True,
        blank=True
    )
    binding = models.ForeignKey(
        Binding,
        on_delete=models.PROTECT,
        related_name='binding',
        verbose_name='Книжный переплет',
    )
    book_format = models.ForeignKey(
        BookFormat,
        on_delete=models.PROTECT,
        related_name='book_format_link',
        verbose_name='Формат'
    )
    book_isbn = models.CharField(
        verbose_name='ISBN',
        max_length=255,
        default='не указано',
    )
    weight = models.FloatField(
        verbose_name='Вес книги, грамм',
        max_length=255,
        help_text='Укажите вес книги в граммах',
        default='не указан',
    )
    age_restrictions = models.ForeignKey(
        AgeRestriction,
        on_delete=models.PROTECT,
        verbose_name='Возрастные ограничения'
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        verbose_name='Издательство'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество книг в наличии'
    )
    book_available = models.BooleanField(
        verbose_name='Доступно для заказа',
        default=False
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        default=10,
        help_text='Значение от 1 до 10',
    )
    inclusion_in_catalog_date = models.DateField(
        verbose_name='Дата внесения в каталог',
        auto_now_add=True
    )
    last_changes_date = models.DateField(
        verbose_name='Дата последнего изменения',
        auto_now=True
    )
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'