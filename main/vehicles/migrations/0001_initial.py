# Generated by Django 3.2.9 on 2022-02-06 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0003_rename_cutomer_name_customers_customer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField()),
                ('return_date', models.DateField()),
                ('vehicle_type', models.CharField(choices=[('bike', 'Bike'), ('cycle', 'Cycle'), ('car', 'Car'), ('boat', 'Boat')], default='bike', max_length=6)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='customers.customers')),
            ],
        ),
    ]