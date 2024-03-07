from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            name = data.get('name')
            email = data.get('email')
            contact = data.get('contact')
            enterprise_id = data.get('enterprise_id')

            if name is None or email is None or contact is None or enterprise_id is None:
                return Response({'message': 'Bad Request: Missing required fields'},
                                status=status.HTTP_400_BAD_REQUEST)
            
            isEmailExists = User.objects.isEmailExist(email)

            if len(isEmailExists) > 0:  ## if an email exists, then email cannot be used again [unique : True]
                return Response({
                    'message': 'User with email already exists', 'Email:': email
                }, status=status.HTTP_406_NOT_ACCEPTABLE)

            User.objects.register_user(name, email, contact, enterprise_id)

            return Response({'message': 'Created: User Registered', 'Name': name, 'Contact': contact},
                            status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({'message': 'Internal Server Error', 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserListView(APIView):
    def get(self, request, enterprise_id, *args, **kwargs):
        try:
            users = User.objects.select_users_by_enterprise_id(enterprise_id)

            if not users:
                return Response({'message': 'No users found for the given enterprise ID'},
                                status=status.HTTP_404_NOT_FOUND)

            user_data = [{'User_ID': user[0], 'Name': user[1]} for user in users]

            return Response({'message': 'Success', 'Users': user_data},
                            status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'message': 'Internal Server Error', 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserIdView(APIView):
    def get(self, request, enterprise_id, *args, **kwargs):
        try:
            user_id = []
            user_id = User.objects.select_user_id_by_enterprise_id(enterprise_id)
            print(User.objects.select_user_id_by_enterprise_id(enterprise_id))

            if user_id is None:
                return Response({'message': 'No user found for the given enterprise ID'},
                                status=status.HTTP_404_NOT_FOUND)

            return Response({'message': 'Success', 'User_ID': user_id},
                            status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'message': 'Internal Server Error', 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)