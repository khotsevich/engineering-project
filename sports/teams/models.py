from django.db import models


class Type(models.Model):
    title = models.CharField(max_length=64, verbose_name='Тип команды')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип команды'
        verbose_name_plural = 'Тип команд'
        ordering = ['title']


class Player(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    surname = models.CharField(max_length=64, verbose_name='Фамилия')
    number = models.IntegerField(verbose_name='Номер')

    def __str__(self):
        return self.surname + ' ' + self.name

    class Meta:
        verbose_name = 'Игроки'
        verbose_name_plural = 'Игрок'
        ordering = ['surname', 'name']


class Team(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Логотип', blank=True)
    players = models.ManyToManyField(Player, verbose_name='Игроки')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип команды')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        ordering = ['name']
