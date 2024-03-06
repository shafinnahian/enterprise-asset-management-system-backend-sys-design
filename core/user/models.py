from django.db import models
from enterprise.models import Enterprise

from django.db import connection

class UserQueryManager(models.Manager):

    def register_user(self, name, contact, enterprise_id):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user_user (name, enterprise_id_id) VALUES (%s, %s)",
                [name, enterprise_id]
            )


    def select_users_by_enterprise_id(self, enterprise_id):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM user_user WHERE enterprise_id_id = %s",
                [enterprise_id]
            )
            print('cursor', cursor)
            result = cursor.fetchall()
        return result


    def select_user_id_by_enterprise_id(self, enterprise_id):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT user_id FROM user_user WHERE enterprise_id_id = %s",
                [enterprise_id]
            )
            result = cursor.fetchall()
        return result

class User (models.Model):
    User_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    contact = models.IntegerField
    Enterprise_ID = models.ForeignKey(Enterprise, on_delete = models.CASCADE)

    objects = UserQueryManager()