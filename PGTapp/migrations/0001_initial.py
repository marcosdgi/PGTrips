# Generated by Django 4.2.3 on 2023-08-09 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('km_recorridos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Salario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('provincia', models.CharField(max_length=50)),
                ('calle', models.CharField(max_length=50)),
                ('numero_casa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Origen', models.CharField(max_length=50)),
                ('Destino', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id_Viaje', models.AutoField(primary_key=True, serialize=False)),
                ('id_auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PGTapp.auto')),
                ('id_chofer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PGTapp.chofer')),
            ],
        ),
        migrations.CreateModel(
            name='Viaje_Destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PGTapp.destino')),
                ('id_viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PGTapp.viaje')),
            ],
        ),
        migrations.CreateModel(
            name='Acompañante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PGTapp.cliente')),
            ],
        ),
    ]
