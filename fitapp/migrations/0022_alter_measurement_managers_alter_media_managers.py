# Generated by Django 4.1.1 on 2022-10-01 07:45

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0021_hydration'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='measurement',
            managers=[
                ('home', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='media',
            managers=[
                ('home', django.db.models.manager.Manager()),
            ],
        ),
    ]
