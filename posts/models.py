from django.db import models

# Create your models here.
class Publication(models.Model):
    body = models.TextField()