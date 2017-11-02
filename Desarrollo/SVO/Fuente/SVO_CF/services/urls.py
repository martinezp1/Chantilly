from django.conf.urls import url


from .views import ListProductAPI

__author__ = 'chris01'

urlpatterns = [

    url(r'^api/v1/products/', ListProductAPI.as_view()),

]
