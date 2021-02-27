from django_filters import rest_framework as filters
from .models import Tour


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TourFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Tour
        fields = ['category', 'date']