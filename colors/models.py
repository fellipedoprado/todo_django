from django.db import models

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=30)
    hexadecimal_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name
    