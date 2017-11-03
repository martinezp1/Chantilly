from django import forms
import django_filters
from rest_framework import filters

from .models import Product, District, Category

__author__ = 'chris01'


class ProductFilter(filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_expr='lte')
    name = django_filters.CharFilter(name="name", lookup_expr='icontains')
    district = django_filters.ModelMultipleChoiceFilter(name="sede__district",
                                                        queryset=District.objects.all(), )
    category = django_filters.ModelMultipleChoiceFilter(name="category",
                                                        queryset=Category.objects.all(), )

    class Meta:
        model = Product
        fields = ['category', 'name', 'min_price', 'max_price', 'district']
