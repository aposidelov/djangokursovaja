from django.db import models

class Restaurant(models.Model):
    title = models.CharField('Назва', max_length=50)
    TYPE_CHOICES = (
        ('coffee_house', 'Кофейня'),
        ('restaurant', 'Ресторан'),
        ('cafe', 'Кофе'),
        ('ready_meal_delivery', 'Доставка готової їжі'),
        ('sushi_bar', 'Суши-бар'),
        ('pizzeria', 'Піццерія'),
        ('fastfood', 'Фаст-фуд'),
    )
    type = models.CharField('Тип', max_length=32, choices=TYPE_CHOICES)
    description = models.TextField('Опис')
    website = models.URLField('Веб-сторінка')
    longitude = models.FloatField('Довгота')
    latitude = models.FloatField('Ширина')
    PRICE_CHOICES = (
        ('$', '$'),
        ('$$', '$$'),
        ('$$$', '$$$'),
    )
    prices = models.CharField('Ціни', max_length=3, choices=PRICE_CHOICES)
    open_hours = models.CharField('Коли відкриті?', max_length=20)
    address = models.CharField('Адреса', max_length=100)
    phone = models.CharField('Телефон', max_length=12)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Ресторани'