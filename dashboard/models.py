from django.db import models

# Create your models here.
class Quimica(models.Model):
    id = models.IntegerField(primary_key=True)
    valor = models.FloatField()
    peso = models.FloatField(default=None)