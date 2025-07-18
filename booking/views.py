from rest_framework import generics, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer
from django.shortcuts import get_object_or_404

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        return Response(
            {
                'booking_id': booking.booking_id,
                'flight': booking.flight.flight_id,
                'status': 'confirmed'
            },
            status=status.HTTP_201_CREATED
        )

class BookingDetailView(generics.RetrieveAPIView):
    queryset = Booking.objects.filter(is_active=True)
    serializer_class = BookingSerializer
    lookup_field = 'booking_id'

    def get_object(self):
        return get_object_or_404(
            Booking, 
            booking_id=self.kwargs['booking_id'],
            is_active=True
        )

class BookingUpdateView(generics.UpdateAPIView):
    queryset = Booking.objects.filter(is_active=True)
    serializer_class = BookingCreateSerializer
    lookup_field = 'booking_id'

class BookingDeleteView(generics.DestroyAPIView):
    queryset = Booking.objects.filter(is_active=True)
    serializer_class = BookingSerializer
    lookup_field = 'booking_id'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()