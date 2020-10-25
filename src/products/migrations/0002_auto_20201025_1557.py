# Generated by Django 3.1.2 on 2020-10-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='inclusion_in_catalog_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в каталог'),
        ),
        migrations.AlterField(
            model_name='book',
            name='last_changes_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
    ]