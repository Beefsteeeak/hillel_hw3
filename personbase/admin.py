from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
