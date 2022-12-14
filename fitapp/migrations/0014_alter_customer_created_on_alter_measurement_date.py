# Generated by Django 4.1.1 on 2022-09-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0013_alter_customer_created_on_alter_measurement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
