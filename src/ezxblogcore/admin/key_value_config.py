from django.contrib import admin
from ..models import KeyValueConfig
# Register your models here.

class KeyValueConfigAdmin(admin.ModelAdmin):
    list_display = ("key", "type", "value")
    list_filter = ("type",)
    search_fields = ("key",)


admin.site.register(KeyValueConfig, KeyValueConfigAdmin)