from django.db import models

# Create your models here.

class bug_details(models.Model):
    SLNO = models.IntegerField(primary_key=True)
    BUGNO = models.IntegerField()
    ASSIGNEE =  models.CharField(max_length=8)
    STATUS = models.IntegerField(max_length=3)
    SUBJECT = models.CharField(max_length=240)
    ENV = models.CharField(max_length=5)

    class Meta:
        db_table = "bug_details"

