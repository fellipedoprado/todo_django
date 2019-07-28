from django.contrib import admin

from core.models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','task', 'description', 'due_date', 'status', 'priority', 'color', 'updated_at', 'created_at', 'user')
    ordering = ('id',)

admin.site.register(Todo, TodoAdmin)
