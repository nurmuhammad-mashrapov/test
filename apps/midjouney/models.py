from django.db import models
from apps.common.models import TimeStampedModel



class Midjouney(TimeStampedModel):
    zapros = models.CharField(max_length=255, verbose_name='Запрос')
    otvet = models.ImageField(upload_to='midjouney', verbose_name='Ответ')


    class Meta:
        verbose_name = 'Midjouney'
        verbose_name_plural = 'Midjouneys'



    def __str__(self):
        return self.zapros



class Struktura(TimeStampedModel):
    zapros = models.CharField(max_length=255, verbose_name='Запрос')
    otvet = models.ImageField(upload_to='struktura', verbose_name='Ответ')


    class Meta:
        verbose_name = 'Struktura'
        verbose_name_plural = 'Strukturas'


    def __str__(self):
        return self.zapros



class Parametr(TimeStampedModel):
    zapros = models.CharField(max_length=255, verbose_name='Запрос')


    class Meta:
        verbose_name = 'Parametr'
        verbose_name_plural = 'Parametrs'


    def __str__(self):
        return self.zapros



class ImageParametr(TimeStampedModel):
    otvet = models.ImageField(upload_to='parametr', verbose_name='Ответ')
    parametr = models.ForeignKey(Parametr, on_delete=models.CASCADE, verbose_name='Параметр')

    class Meta:
        verbose_name = 'ImageParametr'
        verbose_name_plural = 'ImageParametrs'



