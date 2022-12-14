# Generated by Django 4.1.1 on 2022-09-28 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0018_alter_measurement_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['-date']},
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='fit/images')),
                ('type', models.CharField(choices=[('F', 'Front'), ('B', 'Back'), ('S', 'Side')], default=None, max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fitapp.customer')),
            ],
        ),
    ]
