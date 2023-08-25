from django.contrib import admin
from apps.neauralnetwork.models import NeuralNetwork, Tag, Dostup


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Dostup)
class DostupAdmin(admin.ModelAdmin):
    list_display = ('title', )



@admin.register(NeuralNetwork)
class NeuralNetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_18', 'icon_ru')
    list_filter = ('icon_18', 'icon_ru')
    search_fields = ('title', 'description')
    list_editable = ( 'icon_18', 'icon_ru')
    list_per_page = 100
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}