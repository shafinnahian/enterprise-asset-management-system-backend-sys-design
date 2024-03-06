from rest_framework import serializers

class EnterpriseLoginValidation(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()