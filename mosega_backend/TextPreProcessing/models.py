from django.db import models
import jsonfield


# Create your models here.
class TextPreProcessingModel(models.Model):

    # Model Sample attributes

    document_model = jsonfield.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
