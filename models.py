from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Rider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rider_profile")
    phone_number = models.CharField(max_length=20, unique=True)
    preferred_payment_method = models.CharField(max_length=50, blank=True, null=True)
    default_pickup_location = models.CharField(max_length=255, blank=True, null=True)
    profile_photo = models.ImageField(upload_to="rider_profiles/", blank=True, null=True)

    # 🔮 Future fields:
    # wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rider: {self.user.username} ({self.phone_number})"


class Driver(models.Model):
    class AvailabilityStatus(models.TextChoices):
        AVAILABLE = "available", "Available"
        BUSY = "busy", "Busy"
        OFFLINE = "offline", "Offline"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="driver_profile")
    phone_number = models.CharField(max_length=20, unique=True)
    vehicle_make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_number_plate = models.CharField(max_length=20, unique=True)
    driver_license_number = models.CharField(max_length=50, unique=True)
    availability_status = models.CharField(
        max_length=10,
        choices=AvailabilityStatus.choices,
        default=AvailabilityStatus.OFFLINE,
        db_index=True
    )
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    profile_photo = models.ImageField(upload_to="driver_profiles/", blank=True, null=True)

    # 🔮 Future fields:
    # rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)
    # last_ride_completed = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Driver: {self.user.username} ({self.vehicle_number_plate})"

