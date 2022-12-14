# Generated by Django 4.1.3 on 2022-12-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro_Operacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proyecto', models.CharField(max_length=15)),
                ('nombre_proyecto', models.CharField(blank=True, max_length=90, null=True)),
            ],
            options={
                'db_table': 'centros_de_operaciones',
            },
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compania', models.CharField(blank=True, max_length=90, null=True)),
            ],
            options={
                'db_table': 'companias',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(blank=True, max_length=90, null=True)),
                ('cargo', models.CharField(blank=True, max_length=90, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'nominas',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(blank=True, max_length=50, null=True)),
                ('razon_social', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'proovedores',
            },
        ),
    ]
