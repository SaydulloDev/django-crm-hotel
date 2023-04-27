from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=32, null=False, verbose_name='First Name')
    last_name = models.CharField(max_length=32, null=False, verbose_name='Last Name')
    dob = models.DateField(null=False, verbose_name='Brith Date')
    age = models.IntegerField(null=False, verbose_name='Age')
    passport_serial = models.CharField(max_length=32, null=False, verbose_name='Passport')
    image = models.ImageField(upload_to='client_image/', null=False, verbose_name='Image')
    country = models.CharField(max_length=128, null=False, verbose_name='Country')
    region = models.CharField(max_length=128, null=False, verbose_name='Region')
    address = models.CharField(max_length=1024, null=False, verbose_name='Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
