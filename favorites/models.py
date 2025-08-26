import uuid

from django.db import models

from clients.models import Client


class FavoriteProducts(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    client = models.ForeignKey(
        Client,
        null=False,
        blank=False,
        verbose_name='Cliente',
        on_delete=models.CASCADE,
        related_name="client"
    )
    product_id = models.IntegerField(
        null=False,
        verbose_name='Produto',
    )

    class Meta:
        db_table = "favorite_products"
        verbose_name = "Produto favorito"
        verbose_name_plural = "Produtos favoritos"
        unique_together = ['client', 'product_id']
