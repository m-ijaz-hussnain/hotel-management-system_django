from django.contrib import admin
from .models import *

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(HotelAmenity)
class HotelAmenityAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'amenity', 'is_paid')
    list_filter = ('is_paid',)
    search_fields = ('hotel__name', 'amenity__name')

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'property_type',
        'city',
        'owner',
        'is_active',
        'created_at'
    )

    list_filter = (
        'property_type',
        'city',
        'is_active'
    )

    search_fields = (
        'name',
        'city',
        'owner__username',
        'owner__email'
    )

    readonly_fields = ('created_at', 'updated_at')

    inlines = [HotelImageInline]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'hotel',
        'room_type',
        'price',
        'currency',
        'total_rooms',
        'capacity',
        'min_nights',
        'is_active'
    )

    list_filter = (
        'hotel',
        'room_type',
        'currency',
        'is_active'
    )

    search_fields = (
        'hotel__name',
        'room_type__name'
    )
