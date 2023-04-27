from django.db import models

from .client import Client
from .room import Room
from .services import Service


class Guest(models.Model):
    client_info = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Info')
    room_info = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Room Type')
    services = models.ManyToManyField(Service, verbose_name='Services')

    def __str__(self):
        return f'{self.client_info.first_name} - {self.room_info.room_number} - {self.services.name}'
