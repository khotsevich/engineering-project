from django.db import models
from category.models import Category
from django.contrib.auth.models import User


class Podcast(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    audio = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Запись')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкаст'
        verbose_name_plural = 'Подкасты'
        ordering = ['title']
