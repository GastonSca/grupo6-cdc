# Generated by Django 3.2 on 2023-06-05 22:42

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
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('dni', models.CharField(max_length=150)),
                ('fecha_nacimiento', models.DateField(max_length=10)),
                ('telefono', models.CharField(max_length=150)),
            ],
        ),
    ]
