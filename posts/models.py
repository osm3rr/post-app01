from django.db import models

# Create your models here.
class Publication(models.Model):
    body = models.TextField()

    def __str__(self) -> str:
        return self.body[:50]