from django.db import models

# Create your models here.
class studinfo(models.Model):
    sname = models.CharField(max_length=100)
    mail = models.EmailField()
    address = models.CharField(max_length=400)
    phone = models.IntegerField()
    def __str__(self):
        return self.sname
    