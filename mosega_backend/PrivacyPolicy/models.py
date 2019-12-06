from django.db import models
import jsonfield


# Create your models here.
class PrivacyPolicyModel(models.Model):

    # Model sample attributes
    PrivacyPolicy = jsonfield.JSONField()
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    policy_url = models.CharField(max_length=3000, default="")
    policy_heading = models.CharField(max_length=1000, default="")
    type= models.CharField(max_length=100, default="")