from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Device
# Create your views here.

class DeviceRegistration(APIView):
    def post (self, request, *args, **kwargs):
        try:
            data = request.data
            name = data.get('name')
            type = data.get('type')
            deviceModel = data.get('model')
            enterpriseID = data.get('enterprise_id')

            if name is None or type is None or deviceModel is None or enterpriseID is None:
                return Response({'message': 'Bad Request: Missing required fields'},
                                status=status.HTTP_400_BAD_REQUEST)
            
            Device.objects.registerDevice(name, type, deviceModel, enterpriseID)

            return Response({
                            'message': 'Created: Device has been registered',
                            'name': name,
                            'type': type,
                            'model': deviceModel
                        }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'message': 'Internal Server Error', 'error':str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeviceFetchAll(APIView):        
    def get(self, request, enterprise_id, *args, **kwargs):
        try:
            if enterprise_id is None :
                return Response({
                    'message': 'Bad Request: Missing Required Fields'
                }, status = status.HTTP_400_BAD_REQUEST)
            
            result = Device.objects.fetchAllByEnterpriseID(enterprise_id)
            
            # however, result will be without any dictionary
            # hence, we will put each tuple in a dictionary
            processed_data = []

            for device_tuple in result:
                device_id, name, device_type, model, enterprise_id, availability = device_tuple
                processed_data.append({
                    'DeviceID': device_id,
                    'Name': name,
                    'Type': device_type,
                    'DeviceModel': model,
                    'EnterpriseID': enterprise_id,
                    'Availability': availability
                })

            return Response(processed_data, status= status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'message': 'Internal Server Error', 'error':str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeviceAvailability(APIView):
    def get(self, request, enterpriseID, *args, **kwargs):
        try:
            data = request.data
            name = data.get('name')

            if name is None or enterpriseID is None:
                return Response({
                    'message': 'Bad Request: Missing Required Fields'
                }, status = status.HTTP_400_BAD_REQUEST)
            
            result = Device.objects.isDeviceAvailable(name, enterpriseID)

            filteredData = []
            for deviceData in result:
                availability, deviceID = deviceData
                availabilitySTR = ''

                # we are considering, if availability is 0, the device is available
                # if availability != 0, it is not available
                # availability will be dynamically changed everytime the device is checked out/checked in
                if availability == 0:
                    availabilitySTR = 'AVAILABLE'
                else:
                    availabilitySTR = "NOT AVAILABLE"
                
                filteredData.append({
                    'Availability': availabilitySTR,
                    'DeviceID':deviceID
                })
            return Response(filteredData, status= status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'message': 'Internal Server Error', 'error':str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)