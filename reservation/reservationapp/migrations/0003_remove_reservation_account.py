# Generated by Django 3.1.7 on 2021-04-23 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservationapp', '0002_reservation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservationapp',
            name='account',
        ),
    ]