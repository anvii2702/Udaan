"""
URL configuration for flights_tickets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # Frontend
    path('', views.index_user, name='index_user'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('aboutus/', views.about_us, name='about_us'),
    path('contacus/', views.contact_us, name='contact_us'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('flight-listings/', views.flight_listing, name='flight_listing'),
    path('flight-details/<str:flight_key>/<str:fare_id>/', views.flight_details, name='flight_details'),
    path('flight-booking/', views.flight_booking, name='flight_booking'),

    # Dashboard
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('login/', views.my_login, name='login'),
]
