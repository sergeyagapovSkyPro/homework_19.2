from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование',)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
    price = models.FloatField(verbose_name='Цена', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Создан пользователем", **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ('set_published_status', 'Can publish product'),
            ('change_description', 'Can change product description'),
            ('change_category', 'Can change product category'),
        ]

    def __str__(self):
        return f'{self.name} {self.price}'


class Version(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Продукты', related_name='version')
    number_version = models.IntegerField(default=1, verbose_name='Номер версии')
    name_version = models.CharField(max_length=250, verbose_name='Имя версии', default=None)
    version_flag = models.BooleanField(default=False, verbose_name='Признак версии')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.number_version}'
