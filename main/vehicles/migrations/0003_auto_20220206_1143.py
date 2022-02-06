# Generated by Django 3.2.9 on 2022-02-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehicles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicles',
            name='vehicle_type',
        ),
        migrations.AddField(
            model_name='vehicles',
            name='vehicle',
            field=models.CharField(choices=[('bike', 'Bike'), ('cycle', 'Cycle'), ('car', 'Car'), ('boat', 'Boat')], default='bike', max_length=6),
        ),
    ]