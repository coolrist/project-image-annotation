from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255)
    path = models.TextField()
