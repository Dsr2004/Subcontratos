# Generated by Django 4.1.3 on 2022-12-15 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "ModSubcontratos",
            "0007_alter_subcontrato_tipo_contrato_alter_poliza_table_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="subcontrato",
            name="estado",
            field=models.CharField(default="En ejecución", max_length=250),
        ),
    ]
