# Generated by Django 3.2.9 on 2022-12-19 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModSubcontratos', '0010_item_subcontrato'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_subcontrato',
            name='unidad',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
