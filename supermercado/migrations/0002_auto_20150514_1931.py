# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermercado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='colonia',
            field=models.CharField(default=b'Conocido', max_length=150, verbose_name=b'colonia'),
        ),
        migrations.AddField(
            model_name='local',
            name='cp',
            field=models.CharField(max_length=5, null=True, verbose_name=b'Codigo Postal'),
        ),
        migrations.AddField(
            model_name='local',
            name='municipio',
            field=models.CharField(default=b'Conocido', max_length=150, verbose_name=b'Delegacion - Municipio'),
        ),
        migrations.AddField(
            model_name='local',
            name='telefono',
            field=models.CharField(max_length=14, null=True, verbose_name=b'Telefono'),
        ),
    ]
