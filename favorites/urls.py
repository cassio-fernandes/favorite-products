from django.urls import path, include
from rest_framework import routers

from favorites.viewsets import ProductViewSet, FavoriteProductsViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'favorite-products', FavoriteProductsViewSet, basename='favorite-products')

urlpatterns = [
    path('', include(router.urls)),
]