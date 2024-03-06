from django.db import models
from enterprise.models import Enterprise
from user.models import User

class Device (models.Model):
    Device_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    type = models.CharField(max_length = 50)
    deviceModel = models.CharField(max_length = 255)
    Enterprise_ID = models.ForeignKey(Enterprise, on_delete = models.CASCADE)

class DeviceLog (models.Model):
    DeviceLog_ID = models.AutoField(primary_key=True)
    checkout = models.BooleanField
    checkoutTime = models.CharField(max_length = 50)
    checkoutDate = models.CharField(max_length = 50)
    checkoutMonth = models.CharField(max_length = 10)
    checkoutYear = models.IntegerField

    checkin = models.BooleanField
    checkinTime = models.CharField(max_length = 50)
    checkinDate = models.CharField(max_length = 50)
    checkinMonth = models.CharField(max_length = 10)
    checkinYear = models.IntegerField

    Device_ID = models.ForeignKey(Device, on_delete = models.CASCADE)
    User_ID = models.ForeignKey(User, on_delete = models.CASCADE)

# Create your models here.
