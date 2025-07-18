from django.urls import path
from .views import (
    BookingCreateView,
    BookingDetailView,
    BookingUpdateView,
    BookingDeleteView
)

urlpatterns = [
    path('', BookingCreateView.as_view(), name='create-booking'),
    path('<str:booking_id>/', BookingDetailView.as_view(), name='booking-detail'),
    path('<str:booking_id>/update/', BookingUpdateView.as_view(), name='update-booking'),
    path('<str:booking_id>/delete/', BookingDeleteView.as_view(), name='delete-booking'),
]