from django.urls import path
from contrib.users.views import UserViewSet

urlpatterns = [
    path('profile/', UserViewSet.as_view(), name='profile')
]