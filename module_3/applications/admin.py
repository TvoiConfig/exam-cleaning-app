from django.contrib import admin
from .models import ApplicationModel


@admin.register(ApplicationModel)
class ApplicattionAdmin(admin.ModelAdmin):
    pass