# Generated by Django 3.1.2 on 2020-10-20 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directory', '0002_auto_20201020_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Без названия', help_text='Введите название книги', max_length=255, verbose_name='Название книги')),
                ('foto', models.ImageField(upload_to='', verbose_name='Фото обложки')),
                ('price', models.DecimalField(decimal_places=2, help_text='Цена в белорусских рублях', max_digits=6, verbose_name='Цена')),
                ('year_published', models.IntegerField(blank=True, null=True, verbose_name='Год публикации')),
                ('nubmer_of_pages', models.IntegerField(blank=True, null=True, verbose_name='Количество страниц')),
                ('book_isbn', models.CharField(default='не указано', max_length=255, verbose_name='ISBN')),
                ('weight', models.FloatField(default='не указан', help_text='Укажите вес книги в граммах', max_length=255, verbose_name='Вес книги, грамм')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество книг в наличии')),
                ('book_available', models.BooleanField(default=False, verbose_name='Доступно для заказа')),
                ('rating', models.IntegerField(default=10, help_text='Значение от 1 до 10', verbose_name='Рейтинг')),
                ('inclusion_in_catalog_date', models.DateField(auto_now_add=True, verbose_name='Дата внесения в каталог')),
                ('last_changes_date', models.DateField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('age_restrictions', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directory.agerestriction', verbose_name='Возрастные ограничения')),
                ('author', models.ManyToManyField(default='Автор неизвестен', max_length=100, related_name='author', to='directory.Author', verbose_name='ФИО автора')),
                ('binding', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='binding', to='directory.binding', verbose_name='Книжный переплет')),
                ('book_format', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_format_link', to='directory.bookformat', verbose_name='Формат')),
                ('genres', models.ManyToManyField(default='Жанр не указан', max_length=50, related_name='genres', to='directory.Genre', verbose_name='Жанр книги')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directory.publisher', verbose_name='Издательство')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='series', to='directory.series', verbose_name='Серия книг')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
