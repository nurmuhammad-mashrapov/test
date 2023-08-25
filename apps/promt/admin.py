from django.contrib import admin
from apps.promt.models import Promt, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_filter = ('title',)
    search_fields = ('title',)
    list_display_links = ('title',)


@admin.register(Promt)
class PromtAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('is_active',)
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20
    list_display_links = ('title',)
    ordering = ('-order',)



