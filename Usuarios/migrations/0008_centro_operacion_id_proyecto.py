# Generated by Django 4.1.3 on 2022-12-08 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Usuarios", "0007_alter_centro_operacion_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="centro_operacion",
            name="id_proyecto",
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
