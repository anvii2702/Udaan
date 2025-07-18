from rest_framework import serializers
from .models import Flight, Airport

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['code', 'name', 'city', 'country']

# API 1: Flight Search/List Serializer
class FlightSearchSerializer(serializers.ModelSerializer):
    departure_airport = AirportSerializer()
    arrival_airport = AirportSerializer()
    duration = serializers.DurationField(read_only=True)
    
    class Meta:
        model = Flight
        fields = [
            'flight_id',
            'airline',
            'flight_number',
            'departure_airport',
            'arrival_airport',
            'departure_time',
            'arrival_time',
            'duration',
            'economy_price',
            'flight_status'
        ]

# API 2: Flight Detail Serializer
class FlightDetailSerializer(serializers.ModelSerializer):
    departure_airport = AirportSerializer()
    arrival_airport = AirportSerializer()
    
    class Meta:
        model = Flight
        fields = '__all__'
        read_only_fields = ['last_updated', 'created_at']

# API 3: Seat Availability Serializer
class SeatAvailabilitySerializer(serializers.ModelSerializer):
    available_seats = serializers.SerializerMethodField()
    
    class Meta:
        model = Flight
        fields = [
            'flight_id',
            'flight_number',
            'available_seats',
            'economy_price',
            'business_price',
            'first_price'
        ]
    
    def get_available_seats(self, obj):
        return {
            'economy': obj.economy_seats,
            'business': obj.business_seats,
            'first': obj.first_seats
        }