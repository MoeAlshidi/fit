# Generated by Django 4.1.1 on 2022-09-27 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0017_alter_measurement_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['date']},
        ),
    ]
