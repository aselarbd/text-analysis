from django.db import models


# Create your models here.
class SampleAPIModel(models.Model):

    # Model Sample attributes

    name = models.CharField(max_length=100, unique=True)
    heading = models.CharField(max_length=100)
    content = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
