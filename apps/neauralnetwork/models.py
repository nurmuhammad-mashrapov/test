from django.db import models
from apps.common.models import TimeStampedModel


class Tag(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = "Сфера применения"
        verbose_name_plural = "Сферы применения"



    def __str__(self):
        return self.title




class NeuralNetwork(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    link = models.URLField(verbose_name="Ссылка")
    description = models.TextField(verbose_name="Описание")
    zadacha = models.CharField(max_length=255, verbose_name="Задача")
    tag = models.ManyToManyField(Tag, verbose_name="Сфера применения")
    image = models.ImageField(upload_to="neuralnetwork", verbose_name="Изображение")
    free = models.BooleanField(default=False, verbose_name="Бесплатно")
    paid = models.BooleanField(default=False, verbose_name="Платно")
    trial = models.BooleanField(default=False, verbose_name="Триал")
    icon_18 = models.BooleanField(default=False, verbose_name="Иконка 18+")
    icon_ru = models.BooleanField(default=False, verbose_name="Иконка русский язык")
    slug = models.SlugField(max_length=255, verbose_name="Слаг", unique=True)
    order = models.IntegerField(verbose_name="Порядок")

    class Meta:
        verbose_name = "Нейронная сеть"
        verbose_name_plural = "Нейронные сети"
        ordering = ['-order']


    def __str__(self):
        return self.title



