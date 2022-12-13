from django.db import models

restaurant_field_labels = {
    'title': 'Назва',
    'type': 'Тип',
    'description': 'Опис',
    'website': 'Веб-сторінка',
    'longitude': 'Довгота',
    'latitude': 'Ширина',
    'prices': 'Ціни',
    'open_hours': 'Коли відкриті?',
    'address': 'Адреса',
    'phone': 'Телефон',
}

class Restaurant(models.Model):
    title = models.CharField(restaurant_field_labels['title'], max_length=50)
    TYPE_CHOICES = (
        ('coffee_house', 'Кофейня'),
        ('restaurant', 'Ресторан'),
        ('cafe', 'Кофе'),
        ('ready_meal_delivery', 'Доставка готової їжі'),
        ('sushi_bar', 'Суши-бар'),
        ('pizzeria', 'Піццерія'),
        ('fastfood', 'Фаст-фуд'),
    )
    type = models.CharField(restaurant_field_labels['type'], max_length=32, choices=TYPE_CHOICES)
    description = models.TextField(restaurant_field_labels['description'])
    website = models.URLField(restaurant_field_labels['website'])
    longitude = models.FloatField(restaurant_field_labels['longitude'])
    latitude = models.FloatField(restaurant_field_labels['latitude'])
    PRICE_CHOICES = (
        ('$', '$'),
        ('$$', '$$'),
        ('$$$', '$$$'),
    )
    prices = models.CharField(restaurant_field_labels['prices'], max_length=3, choices=PRICE_CHOICES)
    open_hours = models.CharField(restaurant_field_labels['open_hours'], max_length=20)
    address = models.CharField(restaurant_field_labels['address'], max_length=100)
    phone = models.CharField(restaurant_field_labels['phone'], max_length=12)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Ресторани'