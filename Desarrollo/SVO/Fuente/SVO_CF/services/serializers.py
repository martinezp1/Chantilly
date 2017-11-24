from rest_framework import serializers
from .models import Product, District, Category, Promotion

__author__ = 'chris01'

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

