# Generated by Django 4.1.1 on 2022-09-27 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0015_alter_measurement_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='measurement', to='fitapp.customer'),
        ),
    ]
