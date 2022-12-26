# Generated by Django 3.2.9 on 2022-12-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0014_delete_centro_operacion_delete_compania_delete_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo_validador',
            field=models.CharField(choices=[('Ambiental', 'Ambiental'), ('Social', 'Social'), ('RRHH', 'RRHH'), ('Calidad', 'Calidad'), ('SST', 'SST'), ('P&C Planeación', 'P&C Planeación'), ('P&C Costos', 'P&C Costos'), ('Administrador', 'Administrador'), ('Seguros', 'Seguros')], default=1, max_length=150),
            preserve_default=False,
        ),
    ]
