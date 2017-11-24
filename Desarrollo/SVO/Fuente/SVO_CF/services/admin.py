# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Sede, Category, Product, Promotion, District


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'description', 'category']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sede":
            kwargs["queryset"] = Sede.objects.filter(owner=request.user)
        return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sede__owner=request.user)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

