from django.db import models
from apps.common.models import TimeStampedModel


class Category(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    order = models.IntegerField(verbose_name="Порядок")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


    def __str__(self):
        return self.title


class Promt(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    description_ru = models.TextField(verbose_name="Описание на русском")
    description_en = models.TextField(verbose_name="Описание на английском")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    order = models.IntegerField(verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активность")
    slug = models.SlugField(verbose_name="Слаг", unique=True)

    class Meta:
        verbose_name = "Промт"
        verbose_name_plural = "Промты"

    def __str__(self):
        return self.title







