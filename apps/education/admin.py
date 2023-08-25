from django.contrib import admin
from apps.education.models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    list_editable = ('order', 'is_active')



