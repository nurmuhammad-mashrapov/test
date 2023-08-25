from django.contrib import admin
from apps.advertisement.models import Advertisement, AdvertisementTag



@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('title',)
    list_editable = ('is_active', 'order')
    list_display_links = ('title',)



@admin.register(AdvertisementTag)
class AdvertisementTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_banner', 'link_banner', 'image_card', 'link_card', 'image_card_detail', 'link_card_detail', 'promt_image', 'promt_link')
    fieldsets = (
        ("Баннер", {
            'fields': ('image_banner', 'link_banner')
        }),
        ("Карточка", {
            'fields': ('image_card', 'link_card')
        }),
        ("Промт", {
            'fields': ('promt_image', 'promt_link')
        }),
        ("Детальная карточка", {
            'fields': ('image_card_detail', 'link_card_detail')
        }),
    )