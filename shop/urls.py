# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index ,name="ShopHome"),
    path("about", views.about ,name="About Us"),
    path("contact/", views.contact ,name="Contact Us"),
    path("fast/", views.feedback, name="feedback"),
    path("tracker/", views.tracker ,name="TrackingStatus"),
    path("search/", views.search ,name="search"),
    
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout ,name="Checkout"),
    # path("handlerequest/", views.handlerequest, name="HandleRequest")

    # path("", views.index ,name="ShopHome")
]

