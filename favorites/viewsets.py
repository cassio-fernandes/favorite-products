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
    #
    @action(detail=False, methods=['get'])
    def available(self, request):
        products = ProductService.list_products()
        return Response(products)

    @action(detail=False, methods=['post'])
    def favorite(self, request):
        client = request.user.client
        product_ids = request.data.get('product_ids', [])

        created = []
        for _id in product_ids:
            marked_favorite, _ = FavoriteProducts.objects.get_or_create(client=client, product_id=_id)
            created.append(marked_favorite.id)

        return Response({"favorite_products": created}, status=status.HTTP_201_CREATED)
