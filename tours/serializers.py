from rest_framework import serializers

from .models import Tour, TourShot


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'price', 'date', 'image', 'places')
        model = Tour


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("image",)
        model = TourShot


class TourDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    shots = ImageSerializer(many=True)
    payment = serializers.SlugRelatedField(slug_field="payment", read_only=True)

    class Meta:
        fields = ('id', 'title', 'category', 'price', 'desc', 'date', 'image', 'payment', 'places', 'shots')
        model = Tour
