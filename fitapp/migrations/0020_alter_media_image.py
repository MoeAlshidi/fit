# Generated by Django 4.1.1 on 2022-09-30 11:23

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0019_alter_measurement_options_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='fit/images'),
        ),
    ]
