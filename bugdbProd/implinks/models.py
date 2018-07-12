from django.db import models

# Create your models here.
class implinks(models.Model):
    NAME =  models.CharField(max_length=30)
    DESCR = models.CharField(max_length=240)
    LINK = models.CharField(max_length=240)

    class Meta:
        db_table = "implinks"
    def __str__(self):
        return self.NAME

