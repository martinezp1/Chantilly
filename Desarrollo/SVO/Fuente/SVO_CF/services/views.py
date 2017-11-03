# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import RedirectView

from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Product, Category, District, Promotion

from .serializers import ProductSerializer
from .filters import ProductFilter


class ListProductAPI(ListAPIView):
    ''' Filtro: {{Dominio}}/api/v1/products/?category=2&category=1&name=nombre&min_price=&max_price=&district=

    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter

