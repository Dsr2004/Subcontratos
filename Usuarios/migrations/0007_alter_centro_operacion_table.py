# Generated by Django 4.1.3 on 2022-12-07 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Usuarios", "0006_alter_centro_operacion_nombre_proyecto_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="centro_operacion", table="centros_de_operaciones",
        ),
    ]