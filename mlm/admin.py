from django.contrib import admin

from .models import Log


@admin.register(Log)
class LogsModelAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "path", "method"]
