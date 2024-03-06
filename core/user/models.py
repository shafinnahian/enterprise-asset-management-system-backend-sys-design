from django.db import models
from enterprise.models import Enterprise

# Create your models here.
class User (models.Model):
    User_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    contact = models.IntegerField
    Enterprise_ID = models.ForeignKey(Enterprise, on_delete = models.CASCADE)