# Generated by Django 4.1.4 on 2022-12-20 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0007_libro_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Autor activo'),
        ),
    ]
