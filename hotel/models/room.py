from django.db import models


class Room(models.Model):
    class RoomType(models.TextChoices):
        STANDARD = 'standard', 'Standard'
        LUXURY = 'luxury', 'Luxury'
        FAMILY = 'family', 'Family'

    room_type = models.CharField(max_length=50, choices=RoomType.choices, default=RoomType.STANDARD)
    room_number = models.IntegerField(null=False)
    room_image = models.ImageField(upload_to='image_room', null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    bed_count = models.IntegerField(null=False, default=2)

    def __str__(self):
        return self.room_type
