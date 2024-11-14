# Generated by Django 5.1.3 on 2024-11-14 17:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_perfil', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('deporte', models.CharField(choices=[('boxeo', 'Boxeo'), ('kickboxing', 'Kickboxing')], max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='perfil_fotos/')),
                ('genero', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], default='otro', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
