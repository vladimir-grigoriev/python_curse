from django.db import models

class Author(models.Model):
    author_name = models.CharField(verbose_name='ФИО автора', max_length=255)

    def __str__(self):
        return self.author_name


class Series(models.Model):
    series_name = models.CharField(verbose_name='Серия', max_length=255)

    def __str__(self):
        return self.series_name


class Genre(models.Model):
    genre_name = models.CharField(verbose_name='Жанр', max_length=255)

    def __str__(self):
        return self.genre_name


class Publisher(models.Model):
    publisher_name = models.CharField(verbose_name='Издатель', max_length=255)

    def __str__(self):
        return self.publisher_name