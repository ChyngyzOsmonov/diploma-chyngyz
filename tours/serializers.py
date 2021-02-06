from rest_framework import serializers
from .models import Tour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'price', 'date', 'image', 'places')
        model = Tour


class TourDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'price', 'desc', 'date', 'image', 'image2', 'image3', 'image4', 'payment', 'places')
        model = Tour
