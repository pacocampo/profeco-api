from django.db import models
from profeco.models import Producto

# Create your models here.

class Supermercado (models.Model):
	nombre_super = models.CharField(max_length= 100, verbose_name='nombre_del_super')


	def __unicode__(self):
		return self.nombre_super


class Local (models.Model):
	tienda = models.ForeignKey('Supermercado', related_name='supermercado', null=True)
	sucursal = models.CharField(max_length=300, verbose_name='sucursal', default="Conocido")
	direccion = models.CharField(max_length=300, verbose_name='direccion')
	colonia = models.CharField(max_length=150, verbose_name='colonia', default="Conocido")
	municipio = models.CharField(max_length=150, verbose_name='Delegacion - Municipio', default="Conocido")
	cp = models.CharField(max_length=5, verbose_name='Codigo Postal', null=True)
	telefono = models.CharField(max_length=14, verbose_name='Telefono', null=True)
	latitud = models.DecimalField(max_digits=13, decimal_places= 10)
	longitud = models.DecimalField(max_digits=13, decimal_places= 10)

	def __unicode__(self):
		return self.sucursal


class Precio (models.Model):
	local = models.ForeignKey('Local', related_name='locales')
	precio = models.DecimalField(max_digits=9, decimal_places= 4,)
	date_added = models.DateField(auto_now=False, auto_now_add=False)
    	producto = models.ForeignKey(Producto, related_name='precios')

    	def __unicode__(self):
    		return self.precio
