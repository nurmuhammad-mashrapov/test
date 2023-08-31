from django.contrib import admin
from .models import Midjouney


@admin.register(Midjouney)
class MidjouneyAdmin(admin.ModelAdmin):
    pass