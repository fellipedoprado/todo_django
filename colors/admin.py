from django.contrib import admin

# Register your models here.
from colors.models import Color


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'hexadecimal_code',)
    ordering = ('id', 'name')

admin.site.register(Color, ColorAdmin)