# Generated by Django 4.1.3 on 2022-12-27 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ModSubcontratos", "0025_alter_acta_firma_administrador_and_more"),
    ]

    operations = [
        migrations.RenameField(model_name="acta", old_name="estdo", new_name="estado",),
    ]
