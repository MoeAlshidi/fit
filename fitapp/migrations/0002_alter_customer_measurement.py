# Generated by Django 4.1.1 on 2022-09-22 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='measurement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='fitapp.measurement'),
        ),
    ]