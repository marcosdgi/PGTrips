# Generated by Django 4.2.3 on 2023-08-27 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PGTapp', '0003_usuarios_r_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nombre_Usuario',
        ),
        migrations.DeleteModel(
            name='Usuarios_R',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]