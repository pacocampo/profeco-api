# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profeco', '0004_auto_20150512_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=300, verbose_name=b'direccion')),
                ('latitud', models.DecimalField(max_digits=13, decimal_places=10)),
                ('longitud', models.DecimalField(max_digits=13, decimal_places=10)),
            ],
        ),
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.DecimalField(max_digits=5, decimal_places=4)),
                ('date_added', models.DateField()),
                ('local', models.ForeignKey(to='super.Local')),
                ('producto', models.ForeignKey(to='profeco.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Super',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_super', models.CharField(max_length=100, verbose_name=b'nombre_del_super')),
            ],
        ),
        migrations.AddField(
            model_name='local',
            name='super',
            field=models.ForeignKey(verbose_name=b'super', to='super.Super'),
        ),
    ]
