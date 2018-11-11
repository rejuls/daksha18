from django.db import models

# Create your models here.
class rank(models.Model):
    year=models.IntegerField()
    point=models.IntegerField()
