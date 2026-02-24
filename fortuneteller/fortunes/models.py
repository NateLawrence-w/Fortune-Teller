from django.db import models

# Create your models here.
class fortunes(models.Model):
    text = models.CharField(max_length=500) 