# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profeco', '0002_auto_20150511_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preciosuper',
            name='producto',
        ),
        migrations.DeleteModel(
            name='PrecioSuper',
        ),
    ]
