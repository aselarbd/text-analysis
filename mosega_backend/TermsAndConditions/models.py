from django.db import models
import jsonfield


# Create your models here.
class TermsAndConditionsModel(models.Model):

    # Model sample attributes
    Term = jsonfield.JSONField()
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    term_url = models.CharField(max_length=3000, default="")
    term_heading = models.CharField(max_length=1000, default="")
