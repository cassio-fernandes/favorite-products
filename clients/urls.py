from django.urls import path, include
from rest_framework import routers

from clients.viewsets import UserViewSet, ClientViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('clients', ClientViewSet, basename='client')

urlpatterns = [
    path('', include(router.urls)),
]
