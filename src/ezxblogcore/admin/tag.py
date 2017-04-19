from django.contrib import admin
from ..models import Tag
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_time", "modified_time")
    search_fields = ("name",)


admin.site.register(Tag, TagAdmin)