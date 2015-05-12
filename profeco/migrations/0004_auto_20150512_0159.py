# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profeco', '0003_auto_20150511_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=100, verbose_name=b'Categoria')),
                ('imagen', models.ImageField(upload_to=b'', max_length=350, verbose_name=b'Imagen')),
            ],
        ),
        migrations.RenameField(
            model_name='precioprofeco',
            old_name='precioMax',
            new_name='precio_max',
        ),
        migrations.RenameField(
            model_name='precioprofeco',
            old_name='precioMin',
            new_name='precio_min',
        ),
        migrations.RenameField(
            model_name='precioprofeco',
            old_name='precioProm',
            new_name='precio_prom',
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default=b'Marca Libre', max_length=250, verbose_name=b'Descripcion'),
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(default=b'Marca Libre', max_length=100, verbose_name=b'Marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(to='profeco.Categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='presentacion',
            field=models.CharField(default=b'Marca Libre', max_length=300, verbose_name=b'Presentacion'),
        ),
        migrations.DeleteModel(
            name='Categorias',
        ),
    ]
