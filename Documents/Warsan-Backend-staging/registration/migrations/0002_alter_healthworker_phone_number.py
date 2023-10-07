# Generated by Django 3.2.6 on 2023-09-28 15:52

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthworker',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IR', unique=True),
        ),
    ]
