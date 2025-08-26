from django.core.cache import cache
from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from favorites.models import FavoriteProducts
from favorites.serializers import ProductSerializer
from favorites.services import ProductService


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductViewSet(viewsets.ViewSet):
    pagination_class = ProductPagination

    def list(self, request):
        products = ProductService.list_products()
        paginator = self.pagination_class()
        paginated = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(paginated, many=True)

        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        product = ProductService.get_product(pk)
        if not product:
            return response.Response({"detail": "Produto não encontrado"}, status=404)
        serializer = ProductSerializer(product)

        return response.Response(serializer.data)


class FavoriteProductsViewSet(viewsets.ViewSet):
    CACHE_TIMEOUT = 60 * 60 * 24

    @action(detail=False, methods=['get'])
    def available(self, request):
        products = ProductService.list_products()
        return Response(products)

    @action(detail=False, methods=['post'])
    def favorite(self, request):
        client = request.user.client
        product_ids = request.data.get('product_ids', [])

        created = []
        favorites = []
        for _id in product_ids:
            marked_favorite, _ = FavoriteProducts.objects.get_or_create(client=client, product_id=_id)
            created.append(marked_favorite.id)
            product = ProductService.get_product(_id)
            if product:
                favorites.append(product)

        client_favorite_products = cache.get(self.__cache_key(client.id), [])
        favorite_products = {product['id']: product for product in client_favorite_products + favorites}
        cache.set(self.__cache_key(client.id), list(favorite_products.values()), self.CACHE_TIMEOUT)

        return Response({"favorite_products": created}, status=status.HTTP_201_CREATED)

    def list(self, request):
        client = request.user.client
        favorites = cache.get(self.__cache_key(client.id))

        if not favorites:
            product_ids = FavoriteProducts.objects.filter(client=client).values_list("product_id", flat=True)
            favorites = []
            for _id in product_ids:
                product = ProductService.get_product(_id)
                if product:
                    favorites.append(product)
            cache.set(self.__cache_key(client.id), favorites, self.CACHE_TIMEOUT)

        return Response(favorites)

    @staticmethod
    def __cache_key(client_id):
        return f"favorite_products:{client_id}"
