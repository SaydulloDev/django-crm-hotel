# Generated by Django 4.2 on 2023-04-26 14:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=32, verbose_name='Last Name')),
                ('dob', models.DateField(verbose_name='Brith Date')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('passport_serial', models.CharField(max_length=32, verbose_name='Passport')),
                ('image', models.ImageField(upload_to='client_image/', verbose_name='Image')),
                ('country', models.CharField(max_length=128, verbose_name='Country')),
                ('region', models.CharField(max_length=128, verbose_name='Region')),
                ('address', models.CharField(max_length=1024, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('standard', 'Standard'), ('luxury', 'Luxury'), ('family', 'Family')], default='standard', max_length=50)),
                ('room_number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('bed_count', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.client', verbose_name='Info')),
                ('room_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room', verbose_name='Room Type')),
                ('services', models.ManyToManyField(to='hotel.service', verbose_name='Services')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField(default=datetime.date.today)),
                ('check_out_date', models.DateField(default=datetime.date.today)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.client')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
        ),
    ]