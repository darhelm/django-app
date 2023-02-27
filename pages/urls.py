from .views import HomePageView, AboutPageView, BaseView
from django.urls import path

urlpatterns = [path('',BaseView.as_view()),
               path('home/', HomePageView.as_view() , name = "home"),
               path('about/',AboutPageView.as_view(), name = "about")]