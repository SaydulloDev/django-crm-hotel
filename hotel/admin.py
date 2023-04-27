from django.contrib import admin
from .models import Client, Guest, Booking, Room, Service
# Register your models here.
admin.site.register(Client)
admin.site.register(Guest)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(Service)