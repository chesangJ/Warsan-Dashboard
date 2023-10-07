# Generated by Django 3.2.6 on 2023-10-04 09:29

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IR', unique=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.location')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IR')),
                ('position', models.PositiveIntegerField()),
                ('guardian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='child.guardian')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.location')),
            ],
        ),
    ]