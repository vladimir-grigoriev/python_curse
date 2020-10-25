from django.db import models

class Author(models.Model):
    author_name = models.CharField(verbose_name='ФИО автора', max_length=255)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Series(models.Model):
    series_name = models.CharField(verbose_name='Серия', max_length=255)

    def __str__(self):
        return self.series_name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серия'

class Genre(models.Model):
    genre_name = models.CharField(verbose_name='Жанр', max_length=255)

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Publisher(models.Model):
    publisher_name = models.CharField(verbose_name='Издатель', max_length=255)

    def __str__(self):
        return self.publisher_name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

class Binding(models.Model):
    binding_type = models.CharField(
        verbose_name='Тип переплёта',
        max_length=255
    )

    def __str__(self):
        return self.binding_type

    class Meta:
        verbose_name = 'Тип переплёта'
        verbose_name_plural = 'Тип переплёта'

class BookFormat(models.Model):
    book_format = models.CharField(
        verbose_name='Формат',
        max_length=255,
        default='не указан',
    )

    def __str__(self):
        return self.book_format

    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Формат'

class AgeRestriction(models.Model):
    age_restrictions = models.CharField(
        verbose_name='Возрастные ограничения',
        max_length=10,
        default='не указаны',
        help_text='Указываются возрастные ограничения'
    )

    def __str__(self):
        return self.age_restrictions

    class Meta:
        verbose_name = 'Возрастные ограничения'
        verbose_name_plural = 'Возрастные ограничения'