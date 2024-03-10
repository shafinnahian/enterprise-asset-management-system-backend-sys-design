from django.urls import path
from .views import DeviceRegistration, DeviceFetchAll, DeviceAvailability

urlpatterns = [
    path('registerDevice/', DeviceRegistration.as_view(), name='device-registration'),
    path('fetchAllByEntID/<int:enterprise_id>/', DeviceFetchAll.as_view(), name='device-fetchAll'),
    path('isDeviceAvailable/<int:enterpriseID>/', DeviceAvailability.as_view(), name='device-availability')
]