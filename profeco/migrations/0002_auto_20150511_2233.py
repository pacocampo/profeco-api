# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profeco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioProfeco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precioMin', models.DecimalField(max_digits=5, decimal_places=4)),
                ('precioMax', models.DecimalField(max_digits=5, decimal_places=4)),
                ('precioProm', models.DecimalField(max_digits=5, decimal_places=4)),
                ('date_added', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PrecioSuper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.DecimalField(max_digits=5, decimal_places=4)),
                ('date_added', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.CharField(max_length=200, verbose_name=b'Producto')),
                ('presentacion', models.CharField(max_length=300, verbose_name=b'Presentacion')),
                ('categoria', models.ForeignKey(to='profeco.Categorias')),
            ],
        ),
        migrations.AddField(
            model_name='preciosuper',
            name='producto',
            field=models.ForeignKey(to='profeco.Producto'),
        ),
        migrations.AddField(
            model_name='precioprofeco',
            name='producto',
            field=models.ForeignKey(to='profeco.Producto'),
        ),
    ]
