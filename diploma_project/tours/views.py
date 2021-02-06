from rest_framework import generics
from django.shortcuts import render

from .models import Tour
from .serializers import TourSerializer, TourDetailSerializer


class TourList(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class TourDetail(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer
