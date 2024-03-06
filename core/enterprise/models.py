from django.db import models, connections

# Create your models here.

class EnterpriseManager(models.Manager):
    def isEmailExists(self, email):
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM enterprise_enterprise WHERE email = %s", [email])
            result = cursor.fetchall()
        return result

    def registerEnterprise(self, name, email, password, contact):
        with connections['default'].cursor() as cursor:
            cursor.execute("INSERT INTO enterprise_enterprise (name, email, password, address) VALUES (%s, %s, %s, %s)", [name, email, password, contact])

    def getEmailByID(self, enterprise_id):
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT email FROM enterprise_enterprise WHERE enterprise_id = %s", [enterprise_id])
            result = cursor.fetchall()
        return result
    
class Enterprise (models.Model):
    Enterprise_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 255)
    contact = models.IntegerField
    address = models.CharField(max_length = 255)

    objects = EnterpriseManager()