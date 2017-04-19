from django.contrib import admin
from ..models import Media
# Register your models here.

class MediaAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "file", "created_time", "modified_time")
    search_fields = ("name",)
    list_filter = ("type",)


admin.site.register(Media, MediaAdmin)
