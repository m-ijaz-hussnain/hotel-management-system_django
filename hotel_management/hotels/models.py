from django.db import models
from accounts.models import User



# Amenity (Wifi, Parking etc)
class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Hotel 
class Hotel(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='hotels'
    )

    name = models.CharField(max_length=255)
    property_type = models.CharField(
        max_length=50,
        choices=[
            ('hotel', 'Hotel'),
            ('apartment', 'Apartment'),
            ('guest_house', 'Guest House'),
            ('resort', 'Resort'),
        ]
    )

    amenities = models.ManyToManyField(
        Amenity,
        through='HotelAmenity',
        related_name='hotels',
        blank=True
    )

    description = models.TextField()

    star_rating = models.PositiveIntegerField(null=True, blank=True)

    # Location
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    
    # Map location 
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Policies
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()

    is_active = models.BooleanField(default=False)  # Admin approval
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # Date or time for Update 


    def __str__(self):
        return self.name

# Room Type
class RoomType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Room
class Room(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='rooms'
    )
    room_type = models.ForeignKey(
        RoomType,
        on_delete=models.CASCADE,
        related_name='rooms'
    )
    total_rooms = models.PositiveIntegerField(
        help_text="Total rooms of this type in the hotel"
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=10, default='PKR')
    capacity = models.PositiveIntegerField()
    min_nights = models.PositiveIntegerField(default=1)

    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.hotel.name} - {self.room_type}"

# Is-Paid or No-Paid Amenity 
class HotelAmenity(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    class Meta:
        unique_together = ('hotel', 'amenity')

# Image (Cover or Gallary Type)
class HotelImage(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='hotels/')
    is_cover = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hotel.name} Image"
