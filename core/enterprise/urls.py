from django.urls import path
from .views import EnterpriseRegistrationView, EnterpriseLoginView

urlpatterns = [
    path('registerEnterprise/', EnterpriseRegistrationView.as_view(), name='enterprise-registration'),
    path('login/', EnterpriseLoginView.as_view(), name='enterprise-login'),
]