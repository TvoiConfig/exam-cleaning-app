from django.contrib import admin
from .models import ApplicationModel


@admin.register(ApplicationModel)
class ApplicationModelAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "status",)