from django.db import models
from django.conf import settings
from category.models import Category


class News(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    content = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Дата создания')
    updated_at = models.DateTimeField(verbose_name='Дата обновления')
    photo = models.ImageField(verbose_name='Фотография')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
