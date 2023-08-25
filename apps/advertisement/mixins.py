from django.db import models
from django.core.exceptions import ValidationError


class LimitedInstancesModel(models.Model):
    instances_limit = 1

    def clean(self):
        model = self.__class__
        if self.__class__.objects.count() > self.instances_limit - 1 and not model.objects.filter(pk=self.pk):
            raise ValidationError(f'Вы не можете создать более {self.instances_limit} экземпляров модели')

    class Meta:
        abstract = True
