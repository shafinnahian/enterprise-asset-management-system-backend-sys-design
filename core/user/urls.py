from django.urls import path
from .views import UserRegistrationView, UserListView, UserIdView

urlpatterns = [
    path('registerUser/', UserRegistrationView.as_view(), name='user_registration'),
    path('usersListView/<int:enterprise_id>/', UserListView.as_view(), name='user_list_by_enterprise'),
    path('userIdView/<int:enterprise_id>/', UserIdView.as_view(), name='user_id_by_enterprise')
]