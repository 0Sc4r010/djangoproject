# Generated by Django 5.1 on 2024-10-18 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0006_alter_usuarios_rol_alter_usuarios_genero_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
