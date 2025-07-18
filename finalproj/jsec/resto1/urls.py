from django.urls import path

from . import views 

urlpatterns = [
    path("resto1/", views.mainpage, name="resto1"),
    path("resto1/checkout/", views.checkout, name="checkout"),
    path('resto1/confirmation/', views.confirmation, name="confirmation"),
    path("resto1/history/", views.transactions_view, name = 'history')
]