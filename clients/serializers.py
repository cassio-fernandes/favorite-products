from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from clients.models import Client


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ClientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.first_name')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = ["name", "email", "password"]

    def create(self, validated_data):
        email = validated_data.pop("email")
        user = User(username=email, email=email, first_name=validated_data.pop("name"))
        user.set_password(validated_data.pop("password"))

        try:
            with transaction.atomic():
                user.save()
                client = Client.objects.create(user=user)
        except Exception as ex:
            raise serializers.ValidationError(f"Falha ao criar usuário: {ex}")

        return client

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})

        for attr, value in user_data.items():
            setattr(instance.user, attr, value)

        password = validated_data.pop('password', None)
        if password:
            instance.user.set_password(password)

        instance.user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
