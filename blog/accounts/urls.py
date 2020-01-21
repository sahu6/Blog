from django.urls import path,include
from .views import signup,home

urlpatterns = [
    path('signup',signup,name="signup"),
    path('home',home,name="home"),

]
