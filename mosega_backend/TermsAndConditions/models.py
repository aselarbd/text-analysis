from django.db import models


class TermDetails(models.Model):
    class Meta:
        unique_together = (('TermID', 'SectionID'),)

    TermID = models.IntegerField()
    SectionID = models.IntegerField()
    heading = models.CharField(max_length=1000)
    text = models.TextField()

    def __str__(self):
        return self.heading


class TermHighLevel(models.Model):
    tableID = models.AutoField(primary_key=True)
    TermID = models.IntegerField()
    TermURL = models.CharField(max_length=300)
    TermTitle = models.CharField(max_length=1000)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TermTitle
