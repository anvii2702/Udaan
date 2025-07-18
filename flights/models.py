from django.db import models
from django.core.validators import MinValueValidator

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name="IATA Code")
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)  
    timezone = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['city']
        verbose_name_plural = "Airports"

    def __str__(self):
        return f"{self.name} ({self.code})"

class Flight(models.Model):
    FLIGHT_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('delayed', 'Delayed'),
        ('departed', 'Departed'),
        ('arrived', 'Arrived'),
        ('cancelled', 'Cancelled'),
    ]

    flight_id = models.CharField(max_length=10, unique=True)
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=10)
    operating_airline = models.CharField(max_length=100, blank=True)
    flight_status = models.CharField(
        max_length=20,
        choices=FLIGHT_STATUS_CHOICES,
        default='scheduled'
    )
    
    departure_airport = models.ForeignKey(
        Airport,
        related_name='departures',
        on_delete=models.PROTECT
    )
    arrival_airport = models.ForeignKey(
        Airport,
        related_name='arrivals',
        on_delete=models.PROTECT
    )
    
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField()
    
    total_seats = models.PositiveSmallIntegerField()
    economy_seats = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0)]
    )
    business_seats = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0)]
    )
    first_seats = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0)]
    )
    
    economy_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    business_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    first_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['departure_time']
        indexes = [
            models.Index(fields=['flight_number']),
            models.Index(fields=['departure_airport', 'arrival_airport']),
            models.Index(fields=['departure_time']),
        ]

    def save(self, *args, **kwargs):
        if not self.operating_airline:
            self.operating_airline = self.airline
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.airline} {self.flight_number} ({self.departure_airport.code}→{self.arrival_airport.code})"

    @property
    def is_active(self):
        return self.flight_status in ('scheduled', 'delayed')

    @property
    def available_seats(self):
        return {
            'economy': self.economy_seats,
            'business': self.business_seats,
            'first': self.first_seats
        }