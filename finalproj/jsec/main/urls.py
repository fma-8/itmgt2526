from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', views.logout_view, name='logout')
]