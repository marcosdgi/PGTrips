# Generated by Django 4.2.3 on 2023-08-28 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PGTapp', '0004_remove_usuario_nombre_usuario_delete_usuarios_r_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('codigo', models.IntegerField()),
            ],
        ),
    ]
