from django.db import models
from flights.models import Flight
import uuid

class Booking(models.Model):
    SEAT_CLASS_CHOICES = [
        ('economy', 'Economy'),
        ('business', 'Business'),
        ('first', 'First Class'),
    ]
    
    booking_id = models.CharField(
        max_length=10, 
        unique=True,
        default=lambda: uuid.uuid4().hex[:10].upper(),
        editable=False
    )
    flight = models.ForeignKey(
        Flight,
        on_delete=models.PROTECT,
        related_name='bookings'
    )
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    seat_class = models.CharField(max_length=20, choices=SEAT_CLASS_CHOICES)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-booking_date']
        indexes = [
            models.Index(fields=['passenger_email']),
            models.Index(fields=['flight', 'is_active']),
        ]

    def __str__(self):
        return f"{self.booking_id} ({self.flight.flight_number})"

    @property
    def flight_details(self):
        return {
            'flight_id': self.flight.flight_id,
            'airline': self.flight.airline,
            'departure': self.flight.departure_airport.code,
            'arrival': self.flight.arrival_airport.code,
            'time': self.flight.departure_time
        }