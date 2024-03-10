from django.db import models
from enterprise.models import Enterprise
from user.models import User

from django.db import connection

class DeviceQueryManager(models.Manager):
    def registerDevice(self, name, type, deviceModel, enterpriseID):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO device_device (name, type, deviceModel, Enterprise_ID_id, availability) VALUES (%s, %s, %s, %s, 0)",
                [name, type, deviceModel, enterpriseID]
            )
    
    def fetchAllByEnterpriseID(self, enterpriseID):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM device_device WHERE Enterprise_ID_id = %s",
                [enterpriseID]
            )
            result = cursor.fetchall()
            return result
    
    def fetchAllDeviceID_Name_ByEnterpriseID(self, enterpriseID):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT Device_ID, Name FROM device_device WHERE Enterprise_ID_id = %s",
                [enterpriseID]
            )
            result = cursor.fetchall()
            return result

    def isDeviceAvailable(self, Name, enterpriseID):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT availability, Device_ID FROM device_device WHERE name = %s AND Enterprise_ID_id = %s",
                [Name, enterpriseID]
            )
            result = cursor.fetchall()
        return result
    
class DeviceLogQueryManager(models.Manager):
    def checkoutDevice(self, User_ID_id, Device_ID_id, checkoutTime, checkoutDate, checkoutMonth, checkoutYear, checkoutConditionDevice):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO device_devicelog (User_ID_id, Device_ID_id, checkoutTime, checkoutDate, checkoutMonth, checkoutYear, checkoutConditionDevice) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                [ User_ID_id, Device_ID_id, checkoutTime, checkoutDate, checkoutMonth, checkoutYear, checkoutConditionDevice]
            )
    
    def checkinDevice(self, User_ID_id, Device_ID_id, checkinTime, checkinDate, checkinMonth, checkinYear, checkinConditionDevice):
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE SET checkinTime = %s, checkinDate = %s, checkinMonth = %s, checkinYear = %s, checkinConditionDevice = %s WHERE User_ID_id = %s AND Device_ID_id = %s",
                [checkinTime, checkinDate, checkinMonth, checkinYear, checkinConditionDevice, User_ID_id, Device_ID_id]
            )
    

class Device (models.Model):
    Device_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    type = models.CharField(max_length = 50)
    deviceModel = models.CharField(max_length = 255)
    availability = models.BooleanField()
    Enterprise_ID = models.ForeignKey(Enterprise, on_delete = models.CASCADE)

    objects = DeviceQueryManager()

class DeviceLog (models.Model):
    DeviceLog_ID = models.AutoField(primary_key=True)
    checkout = models.BooleanField
    checkoutTime = models.CharField(max_length = 50)
    checkoutDate = models.CharField(max_length = 50)
    checkoutMonth = models.CharField(max_length = 10)
    checkoutYear = models.IntegerField()
    checkoutConditionDevice = models.CharField(max_length = 255)

    checkin = models.BooleanField
    checkinTime = models.CharField(max_length = 50)
    checkinDate = models.CharField(max_length = 50)
    checkinMonth = models.CharField(max_length = 10)
    checkinYear = models.IntegerField()
    checkinConditionDevice = models.CharField(max_length = 255)

    Device_ID = models.ForeignKey(Device, on_delete = models.CASCADE)
    User_ID = models.ForeignKey(User, on_delete = models.CASCADE)

# Create your models here.
