# Generated by Django 3.2.7 on 2021-10-01 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0003_rename_returndata_booking_returndate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]