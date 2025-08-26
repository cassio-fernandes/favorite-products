import logging
import os

import requests
from django.core.cache import cache
from core.settings import CACHE_TTL
from favorites.serializers import ListProductSerializer


class ProductService:
    BASE_URL = os.environ.get('PRODUCT_SERVICE_HOST')
    CACHE_KEY = 'product_catalog'

    @classmethod
    def list_products(cls):
        products = cache.get(cls.CACHE_KEY)
        if products is not None:
            return products

        response = requests.get(cls.BASE_URL + "/products")
        if response.status_code == 200:
            products = response.json()
            cache.set(cls.CACHE_KEY, products, CACHE_TTL)
            return products
        return []

    @classmethod
    def get_product(cls, product_id):
        response = requests.get(f"{cls.BASE_URL}/products/{product_id}/")
        if response.status_code == 200:
            serializer = ListProductSerializer(data=response.json())
            serializer.is_valid(raise_exception=True)

            return serializer.data
        return None
