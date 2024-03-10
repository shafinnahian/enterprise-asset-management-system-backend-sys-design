from django.db import models
from enterprise.models import Enterprise

from django.db import connection

class UserQueryManager(models.Manager):

    # def register_user(self, name, email, contact, enterprise_id):
    #     with connection.cursor() as cursor:
    #         cursor.execute(
    #             "INSERT INTO user_user (name, email, contact, enterprise_id_id) VALUES (%s, %s, %s, %s)",
    #             (name, email, contact, enterprise_id)
    #         )
    def register_user(self, name, email, contact, enterprise_id):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user_user (name, email, contact, enterprise_id_id) VALUES (%s, %s, %s, %s)",
                [name, email, contact, enterprise_id]
            )
    
    def isEmailExist(self, email):
        print(email)
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT user_id FROM user_user WHERE email = %s",
                [email]
            )
            result = cursor.fetchone()
            print(result)
            return result if result else []


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
    email = models.EmailField(unique = True)
    contact = models.IntegerField(null = True)
    Enterprise_ID = models.ForeignKey(Enterprise, on_delete = models.CASCADE)

    objects = UserQueryManager()