# Generated by Django 3.1.2 on 2020-12-01 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20201129_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('var1', 'Принят в обработку'), ('var2', 'Обработан'), ('var3', 'Оплачен, формируется к отгрузке'), ('var4', 'Отправлен, '), ('var5', 'Не отвечает на звонок'), ('var6', 'Отменён покупателем')], default='var1', max_length=4, verbose_name='Статус'),
        ),
    ]
