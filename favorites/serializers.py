from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField(allow_blank=True, required=False)
    category = serializers.CharField()
    image = serializers.CharField()


class RatingSerializer(serializers.Serializer):
    rate = serializers.FloatField()
    count = serializers.IntegerField()


class ListProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.FloatField()
    image = serializers.CharField()
    rating = RatingSerializer(required=False)
