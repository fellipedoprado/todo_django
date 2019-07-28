from django.contrib import admin

from priorities.models import Priority
# Register your models here.
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    ordering = ('id',)

admin.site.register(Priority, PriorityAdmin)