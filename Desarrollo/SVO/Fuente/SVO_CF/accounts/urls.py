__author__ = 'chris01'

from django.conf.urls import url

from .views import CreateUserAPI

urlpatterns = [
    url(r'^api/v1/users/', CreateUserAPI.as_view()),
]
