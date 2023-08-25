from django.db import models
from apps.common.models import TimeStampedModel

from apps.advertisement.mixins import LimitedInstancesModel


class Advertisement(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to="advertisement", verbose_name="Изображение")
    link = models.URLField(verbose_name="Ссылка")
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    order = models.IntegerField(verbose_name="Порядок")

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"


    def __str__(self):
        return self.title


class AdvertisementTag(LimitedInstancesModel):
    instances_limit = 1
    image_banner = models.ImageField(upload_to="advertisement", blank=True, verbose_name="Изображение баннера")
    link_banner = models.URLField(blank=True, verbose_name="Ссылка")
    image_card = models.ImageField(upload_to="advertisement", blank=True, verbose_name="Изображение карточки")
    link_card = models.URLField(blank=True, verbose_name="Ссылка")
    image_card_detail = models.ImageField(upload_to="advertisement",  blank=True, verbose_name="Изображение карточки детально")
    link_card_detail = models.URLField(blank=True,  verbose_name="Ссылка")
    promt_image = models.ImageField(upload_to="advertisement",  blank=True, verbose_name="Изображение промта")
    promt_link = models.URLField(blank=True, verbose_name="Ссылка")


    class Meta:
        verbose_name = "Тег рекламы"
        verbose_name_plural = "Теги рекламы"

    def __str__(self):
        if self.image_banner:
            return self.image_banner.url
        elif self.link_banner:
            return self.link_banner
        elif self.image_card:
            return self.image_card.url
        else:
            return self.link_card

