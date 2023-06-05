# Generated by Django 3.2 on 2023-06-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('dni', models.IntegerField(verbose_name='DNI')),
            ],
        ),
    ]
