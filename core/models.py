from datetime import datetime

from django.db import models

from colors.models import Color
from priorities.apps import PrioritiesConfig
from priorities.models import Priority
from status.models import Status

# Create your models here.
from users.models import User


class Todo(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=5,  blank=True, null=True)
    priority = models.CharField(max_length=5,  blank=True, null=True)
    color = models.CharField(max_length=5,  blank=True, null=True)
    #status = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True)
    #priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, blank=True, null=True)
    #color = models.OneToOneField(Color, on_delete=models.SET_NULL, blank=True, null=True)
    #fazer created at e updated at
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

    def get_priority(self):
        priority = Priority.objects.get(id=self.priority)
        return priority.name.capitalize()

    def get_status(self):
        status = Status.objects.get(id=self.status)
        return status.name.capitalize()

    def get_due_date(self):
        return self.due_date.strftime('%Y-%m-%d')