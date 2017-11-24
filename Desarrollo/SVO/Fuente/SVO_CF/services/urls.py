from django.conf.urls import url


from .views import ListProductAPI, ListCategoryAPI

__author__ = 'chris01'

urlpatterns = [

    url(r'^api/v1/products/', ListProductAPI.as_view()),
    url(r'^api/v1/categories/', ListCategoryAPI.as_view()),

]
