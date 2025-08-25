from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="client"
    )
    name = models.CharField(
        max_length=150,
        verbose_name='Nome'
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )

    class Meta:
        db_table = "client"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

        constraints = [
            models.UniqueConstraint(fields=['name', 'email'], name='unique_name_email_client')
        ]

    def __str__(self):
        return f"{self.name} ({self.email})"