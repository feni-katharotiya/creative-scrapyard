# from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path("", views.home ,name="ShopHome"),
    path("about", views.about ,name="About Us"),
    path("contact/", views.contact ,name="Contact Us"),
    path("tracker/", views.tracker ,name="TrackingStatus"),
    path("search/", views.search ,name="search"),
    path("productView/", views.productView ,name="ProductView"),
    path("checkout/", views.checkout ,name="Checkout")
    # path("", views.index ,name="ShopHome")
]