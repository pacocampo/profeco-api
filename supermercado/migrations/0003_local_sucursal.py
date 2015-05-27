# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermercado', '0002_auto_20150514_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='sucursal',
            field=models.CharField(default=b'Conocido', max_length=300, verbose_name=b'sucursal'),
        ),
    ]
