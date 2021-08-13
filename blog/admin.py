from django.contrib import admin

# Register your models here.
from .models import ArtikelModel


class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'publish',
        'update',
        'slug',
    ]


admin.site.register(ArtikelModel, ArtikelAdmin)
