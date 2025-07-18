from rest_framework import serializers
from .models import Booking
from flights.serializers import FlightSearchSerializer

class BookingSerializer(serializers.ModelSerializer):
    flight = FlightSearchSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'flight',
            'passenger_name',
            'passenger_email',
            'seat_class',
            'booking_date'
        ]
        read_only_fields = ['booking_id', 'booking_date']

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'flight',
            'passenger_name',
            'passenger_email',
            'seat_class'
        ]

    def validate(self, data):
        flight = data['flight']
        seat_class = data['seat_class']
        
        # Check seat availability
        if seat_class == 'economy' and flight.economy_seats <= 0:
            raise serializers.ValidationError("No economy seats available")
        elif seat_class == 'business' and flight.business_seats <= 0:
            raise serializers.ValidationError("No business seats available")
        elif seat_class == 'first' and flight.first_seats <= 0:
            raise serializers.ValidationError("No first class seats available")
            
        return data