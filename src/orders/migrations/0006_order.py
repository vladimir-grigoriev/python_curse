# Generated by Django 3.1.2 on 2020-11-23 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20201123_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=40, verbose_name='E-mail')),
                ('delivery', models.CharField(choices=[('pu', 'Самовывоз'), ('cr', 'Доставка курьером'), ('pt', 'Доставка почтой')], default='pu', max_length=2, verbose_name='Доставка')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('already_paid', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='orders.cart', verbose_name='Order')),
            ],
        ),
    ]