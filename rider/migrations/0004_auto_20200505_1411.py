# Generated by Django 3.0.5 on 2020-05-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0003_ride_driverid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='driverId',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
