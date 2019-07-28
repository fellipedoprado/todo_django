from django.contrib import admin

from status.models import Status
# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    ordering = ('id',)

admin.site.register(Status, StatusAdmin)