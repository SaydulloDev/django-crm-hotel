from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=256, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
