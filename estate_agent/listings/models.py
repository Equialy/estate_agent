from django.db import models
from users.models import UserProfile


class Listings(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('inactive', 'Неактивно'),
        ('sold', 'Продано'),
    ]
    TYPE_CHOICES = [
        ('sale', 'Продажа'),
        ('rent', 'Аренда'),
    ]
    PROPERTY_CHOICES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('commercial', 'Коммерческая'),
    ]

    title = models.CharField(max_length=255,null=True, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена")
    area = models.DecimalField(max_digits=8, decimal_places=2, null=True, verbose_name="Площадь (м²)")
    rooms = models.PositiveIntegerField(null=True,verbose_name="Комнат")
    transaction_type = models.CharField(max_length=10,null=True, choices=TYPE_CHOICES, verbose_name="Тип сделки")
    property_type = models.CharField(max_length=20,null=True, choices=PROPERTY_CHOICES, verbose_name="Тип недвижимости")
    status = models.CharField(max_length=10,null=True, choices=STATUS_CHOICES, default='active', verbose_name="Статус")
    address = models.CharField(max_length=255, null=True, verbose_name="Адрес")
    city = models.CharField(max_length=100,null=True, verbose_name="Город")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='listings',
        null=True,
        verbose_name='Агент'
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']

    def __str__(self):
        return self.title