from django.db import models

class Author(models.Model):
    """Справочник авторов"""
    author_name = models.CharField(
        verbose_name='ФИО автора',
        max_length=255,
    )
    foto = models.ImageField(
        verbose_name='Изображение',
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Сведения об авторе',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.author_name
    
    @classmethod
    def get_class_url(self):
        return 'authors'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Series(models.Model):
    """Справочник серий книг"""
    series_name = models.CharField(
        verbose_name='Серия',
        max_length=255
    )
    author = models.ForeignKey(
        Author,
        verbose_name= 'Автор',
        on_delete = models.PROTECT,
        related_name= 'series',
        null=True
    )

    def __str__(self):
        return self.series_name

    @classmethod
    def get_class_url(self):
        return 'series'
    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серия'


class Genre(models.Model):
    """Справочник жанров книг"""
    genre_name = models.CharField(
        verbose_name='Жанр',
        max_length=255
    )

    def __str__(self):
        return self.genre_name

    @classmethod
    def get_class_url(self):
        return 'genres'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Publisher(models.Model):
    """Справочник издательств"""
    publisher_name = models.CharField(
        verbose_name='Издатель',
        max_length=255
    )

    def __str__(self):
        return self.publisher_name

    @classmethod
    def get_class_url(self):
        return 'publishers'

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Binding(models.Model):
    """Справочник переплётов книг"""
    binding_type = models.CharField(
        verbose_name='Тип переплёта',
        max_length=255
    )

    def __str__(self):
        return self.binding_type

    @classmethod
    def get_class_url(self):
        return 'binding'

    class Meta:
        verbose_name = 'Тип переплёта'
        verbose_name_plural = 'Тип переплёта'


class BookFormat(models.Model):
    """Справочник книжных форматов"""
    book_format = models.CharField(
        verbose_name='Формат',
        max_length=255,
    )

    def __str__(self):
        return self.book_format

    @classmethod
    def get_class_url(self):
        return 'book_formats'

    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Формат'


class AgeRestriction(models.Model):
    """Справочник возрастных ограничений"""
    age_restrictions = models.CharField(
        verbose_name='Возрастные ограничения',
        max_length=10,
        help_text='Указываются возрастные ограничения'
    )

    def __str__(self):
        return self.age_restrictions

    @classmethod
    def get_class_url(self):
        return 'age_restrictions'

    class Meta:
        verbose_name = 'Возрастные ограничения'
        verbose_name_plural = 'Возрастные ограничения'