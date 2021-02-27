from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', TourDetail.as_view(), name='tour-detail'),
    path('', TourList.as_view(), name='tour-list'),
    path('category/', CategoryList.as_view(), name='category-list'),
]
