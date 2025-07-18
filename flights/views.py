from rest_framework import generics
from django.db.models import Q
from .models import Flight
from .serializers import FlightSearchSerializer, FlightDetailSerializer, FlightAvailabilitySerializer
from datetime import datetime


class FlightSearchAPIView(generics.ListAPIView):
    serializer_class = FlightSearchSerializer
    
    def get_queryset(self):
        queryset = Flight.objects.all()
        
    
        airline = self.request.query_params.get('airline')
        departure_code = self.request.query_params.get('from')
        arrival_code = self.request.query_params.get('to')
        date = self.request.query_params.get('date')
        max_price = self.request.query_params.get('max_price')
        
        
        filters = Q()
        if airline:
            filters &= Q(airline__icontains=airline)
        if departure_code:
            filters &= Q(departure_airport__code=departure_code)
        if arrival_code:
            filters &= Q(arrival_airport__code=arrival_code)
        if date:
            try:
                date_obj = datetime.strptime(date, '%Y-%m-%d').date()
                filters &= Q(departure_time__date=date_obj)
            except ValueError:
                pass
        if max_price:
            try:
                filters &= Q(economy_price__lte=float(max_price))
            except (ValueError, TypeError):
                pass
        
        return queryset.filter(filters).order_by('departure_time')


class FlightDetailAPIView(generics.RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightDetailSerializer
    lookup_field = 'flight_id'


class FlightAvailabilityAPIView(generics.RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightAvailabilitySerializer
    lookup_field = 'flight_id'