# Generated by Django 4.1.3 on 2022-12-20 22:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("ModSubcontratos", "0012_alter_subcontrato_validadores"),
    ]

    operations = [
        migrations.AddField(
            model_name="subcontrato",
            name="fecha_creacion",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subcontrato",
            name="proximo_envio_correo",
            field=models.DateField(default="2022-12-20"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="subcontrato",
            name="estado",
            field=models.CharField(
                choices=[
                    ("1", "En ejecución"),
                    ("2", "No ejecutado"),
                    ("3", "Suspendido"),
                    ("4", "Liquidado"),
                ],
                max_length=30,
            ),
        ),
    ]
