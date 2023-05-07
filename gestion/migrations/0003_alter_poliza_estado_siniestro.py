# Generated by Django 4.2 on 2023-05-02 04:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_poliza_actualizaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poliza',
            name='estado',
            field=models.CharField(blank=True, choices=[('Vigente', 'Vigente'), ('Vencida', 'Vencida'), ('Inactivo', 'Inactivo')], default='Vigente', max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Siniestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_siniestro', models.DateField(default=datetime.datetime.now)),
                ('cliente', models.CharField(blank=True, max_length=255, null=True)),
                ('vencimiento_siniestro', models.DateField(default=datetime.datetime.now)),
                ('estado', models.CharField(choices=[('Recibido', 'Recibido'), ('En Proceso', 'En Proceso'), ('En Espera', 'En Espera'), ('Finalizado', 'Finalizado')], default='Recibido', max_length=20)),
                ('nombre_tercero', models.CharField(max_length=255)),
                ('documento_tercero', models.CharField(max_length=255)),
                ('compania_tercero', models.CharField(max_length=255)),
                ('poliza_tercero', models.CharField(max_length=255)),
                ('patente_tercero', models.CharField(max_length=255)),
                ('vehiculo_tercero', models.CharField(max_length=255)),
                ('lugar_tercero', models.CharField(max_length=255)),
                ('localidad_tercero', models.CharField(max_length=255)),
                ('telefono_tercero', models.CharField(max_length=255)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('poliza_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion.poliza')),
            ],
        ),
    ]
