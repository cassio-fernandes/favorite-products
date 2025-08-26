import uuid

from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="client"
    )

    class Meta:
        db_table = "client"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.user.get_full_name() or self.user.username
