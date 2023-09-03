# Generated by Django 4.2.3 on 2023-08-23 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PGTapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='Fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='Hora',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]