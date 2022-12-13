# Generated by Django 3.2.16 on 2022-12-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('type', models.CharField(choices=[('coffee_house', 'Кофейня'), ('restaurant', 'Ресторан'), ('cafe', 'Кофе'), ('ready_meal_delivery', 'Доставка готової їжі'), ('sushi_bar', 'Суши-бар'), ('pizzeria', 'Піццерія'), ('fastfood', 'Фаст-фуд')], max_length=32, verbose_name='Тип')),
                ('description', models.TextField(verbose_name='Опис')),
                ('website', models.URLField(verbose_name='Веб-сторінка')),
                ('longitude', models.FloatField(verbose_name='Довгота')),
                ('latitude', models.FloatField(verbose_name='Ширина')),
                ('prices', models.CharField(choices=[('$', '$'), ('$$', '$$'), ('$$$', '$$$')], max_length=3, verbose_name='Ціни')),
                ('open_hours', models.CharField(max_length=20, verbose_name='Коли відкриті?')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('address', models.CharField(max_length=100, verbose_name='Адреса')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
            ],
        ),
    ]