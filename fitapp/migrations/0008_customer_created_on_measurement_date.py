# Generated by Django 4.1.1 on 2022-09-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0007_alter_customer_user_alter_measurement_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_on',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
