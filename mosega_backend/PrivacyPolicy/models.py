from django.db import models


class PolicyDetails(models.Model):
    class Meta:
        unique_together = (('PolicyID', 'SectionID'),)

    PolicyID = models.IntegerField()
    SectionID = models.IntegerField()
    heading = models.CharField(max_length=1000)
    text = models.TextField()

    def __str__(self):
        return self.heading


class PolicyHighLevel(models.Model):
    tableID = models.AutoField(primary_key=True)
    PolicyID = models.IntegerField()
    PolicyURL = models.CharField(max_length=300)
    PolicyTitle = models.CharField(max_length=1000)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PolicyTitle
