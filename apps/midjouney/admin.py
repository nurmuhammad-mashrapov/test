from django.contrib import admin
from .models import Midjouney, Struktura, Parametr, ImageParametr


@admin.register(Midjouney)
class MidjouneyAdmin(admin.ModelAdmin):
    pass


@admin.register(Struktura)
class StrukturaAdmin(admin.ModelAdmin):
    pass


@admin.register(Parametr)
class ParametrAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageParametr)
class ImageParametrAdmin(admin.ModelAdmin):
    pass