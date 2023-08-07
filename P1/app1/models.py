from django.db import models

# Create your models here.

class details(models.Model):
    name = models.CharField('name',max_length=10)
    age = models.IntegerField('name',max_length=10)
