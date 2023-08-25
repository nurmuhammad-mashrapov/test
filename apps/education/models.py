from django.db import models
from apps.common.models import TimeStampedModel


class Education(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="education", verbose_name="Изображение")
    order = models.IntegerField(verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активность")
    slug = models.SlugField(verbose_name="Слаг", unique=True)

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"

    def __str__(self):
        return self.title