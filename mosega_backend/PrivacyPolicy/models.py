from django.db import models
import jsonfield


# Create your models here.
class PrivacyPolicyModel(models.Model):

    # Model sample attributes
    PrivacyPolicy = jsonfield.JSONField()
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
