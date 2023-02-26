from .views import response
from django.urls import path

urlpatterns = [path('', response, name = "home"),]