# Generated by Django 5.1.3 on 2024-11-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_perfil_edad_perfil_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='genero',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('prefiero no decir', 'Prefiero no decir')], default='otro', max_length=20),
        ),
    ]
