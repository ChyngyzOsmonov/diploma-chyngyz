from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Tour, Category
from .serializers import TourSerializer, TourDetailSerializer, CategorySerializer
from .service import TourFilter


class TourList(generics.ListAPIView):
    queryset = Tour.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TourFilter
    serializer_class = TourSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TourDetail(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer
