# Generated by Django 3.2.9 on 2022-02-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('bike', 'Bike'), ('cycle', 'Cycle'), ('car', 'Car'), ('boat', 'Boat')], max_length=6)),
                ('count', models.IntegerField()),
            ],
        ),
    ]