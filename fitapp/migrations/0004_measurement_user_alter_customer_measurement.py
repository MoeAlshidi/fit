# Generated by Django 4.1.1 on 2022-09-22 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0003_alter_customer_measurement'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET, related_name='+', to='fitapp.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='measurement',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='fitapp.measurement'),
        ),
    ]