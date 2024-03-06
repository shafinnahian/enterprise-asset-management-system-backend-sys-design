from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Enterprise
from .serializer import EnterpriseLoginValidation
from django.contrib.auth.hashers import make_password, check_password
import jwt
from django.conf import settings

class EnterpriseRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            contact = data.get('contact')

            if name is None or email is None or password is None:
                return Response({'message': 'Bad Request: Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

            isEmailExists = Enterprise.objects.isEmailExists(email)   # Error handling: Checking for email's existence

            if isEmailExists:
                return Response(
                    {'message': 'Conflict: Account with email exists', 'Email': isEmailExists[0]['email']},
                    status=status.HTTP_409_CONFLICT
                )

            # models.py has the original MySQL query written, it has been called here for better code structuring
            Enterprise.objects.registerEnterprise(name, email, password, contact)

            return Response({'message': 'Created: Enterprise Registered', 'Name': name, 'Email': email},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': 'Internal Server Error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EnterpriseLoginView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = EnterpriseLoginValidation(data=data) #Validating the inputs 

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')

            # Error handling: Checking for email's existence
            enterpriseData = Enterprise.objects
            isEmailExists = enterpriseData.isEmailExists(email)

            if not isEmailExists:
                return Response({'message': 'Email not registered'}, status=status.HTTP_404_NOT_FOUND)

            enterprise = isEmailExists[0]  # isEmailExists = true. Hence array.
            print(enterprise, password)
            if not (password == enterprise[3]):
                return Response({'message': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

            # To generate a token for payload
            jwt_secret = 'zw2983y458q3y4fcfvghbjnk578vq783rtyy8gf'
            expirationInSeconds = 24 * 60 * 60  # 24 hours, but in seconds

            tokenPayload = {
                'Email': enterprise[2],
                'Enterprise_ID': enterprise[0],
                'loginExpiration': expirationInSeconds
            }

            tokenBytes = jwt.encode(tokenPayload, jwt_secret, algorithm='HS256')
            # token = tokenBytes.decode('utf-8')

            return Response({'enterprise': tokenPayload, 'token': tokenBytes}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'message': 'Required fields are undefined', 'errors': serializer.errors},
                status=status.HTTP_401_UNAUTHORIZED
            )
