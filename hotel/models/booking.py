from datetime import date

from django.db import models

from .client import Client
from .room import Room


class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room_type = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField(default=date.today)
    check_out_date = models.DateField(default=date.today)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.client} - {self.room_type} - {self.check_in_date} to {self.check_out_date} - ' \
               f'{self.price}'
