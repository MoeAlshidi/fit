# Generated by Django 4.1.1 on 2022-09-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0011_alter_customer_age_alter_customer_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
