from django.db import models
from category.models import Category
from teams.models import Team


class Sponsor(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Логотип', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спонсор'
        verbose_name_plural = 'Спонсоры'
        ordering = ['name']


class Tournament(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    prize_fund = models.IntegerField(verbose_name='Призовой фонд')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, verbose_name='Спонсор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
        ordering = ['name']


class Event(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    time = models.DateTimeField(verbose_name='Время проведения')
    result = models.CharField(max_length=64, verbose_name='Результат', blank=True)
    status = models.CharField(max_length=64, verbose_name='Статус')
    teams = models.ManyToManyField(Team, verbose_name='Команды')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, verbose_name='Турнир')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['name']

