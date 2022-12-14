# Generated by Django 3.2.9 on 2022-12-05 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('usuario', models.CharField(max_length=50, unique=True, verbose_name='Nombre de Usuario')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=25, verbose_name='Apellidos')),
                ('correo', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('cedula', models.CharField(max_length=15, unique=True, verbose_name='Cedula')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado del usuario')),
                ('administrador', models.BooleanField(default=False)),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rol', to='auth.group')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
