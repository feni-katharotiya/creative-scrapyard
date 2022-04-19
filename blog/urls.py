# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name="ShopHome"),
    path("fast/", views.help, name="help"),
    
    
]
