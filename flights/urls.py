from django.urls import path
from .views import FlightSearchAPIView, FlightDetailAPIView, FlightAvailabilityAPIView

urlpatterns = [
    path('search/', FlightSearchAPIView.as_view(), name='flight-search'),
    path('<str:flight_id>/', FlightDetailAPIView.as_view(), name='flight-detail'),
    path('<str:flight_id>/availability/', FlightAvailabilityAPIView.as_view(), name='flight-availability'),
]