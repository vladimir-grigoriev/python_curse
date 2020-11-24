# Generated by Django 3.1.2 on 2020-11-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_series_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Сведения об авторе'),
        ),
        migrations.AddField(
            model_name='author',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='agerestriction',
            name='age_restrictions',
            field=models.CharField(help_text='Указываются возрастные ограничения', max_length=10, verbose_name='Возрастные ограничения'),
        ),
        migrations.AlterField(
            model_name='bookformat',
            name='book_format',
            field=models.CharField(max_length=255, verbose_name='Формат'),
        ),
    ]