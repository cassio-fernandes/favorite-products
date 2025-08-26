from rest_framework import viewsets, response
from rest_framework.pagination import PageNumberPagination

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
