# Generated by Django 3.2.9 on 2022-02-05 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20220205_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='cutomer_name',
            new_name='customer_name',
        ),
    ]