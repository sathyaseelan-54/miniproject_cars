# Generated by Django 3.2.7 on 2021-10-01 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0004_alter_booking_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='lastname',
        ),
    ]