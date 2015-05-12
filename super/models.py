from django.db import models
from profeco.models import Producto

# Create your models here.

class Super (models.Model):
	nombre_super = models.CharField(max_length= 100, verbose_name='nombre_del_super')


	def __unicode__(self):
		return self.nombre_super


class Local (models.Model):
	super = models.ForeignKey(Super, verbose_name='super')
	direccion = models.CharField(max_length=300, verbose_name='direccion')
	latitud = models.DecimalField(max_digits=3, decimal_places= 10)
	longitud = models.DecimalField(max_digits=3, decimal_places= 10)

	def __unicode__(self):
		return self.super


class Precios (models.Model):
	local = models.ForeignKey('Local')
	precio = models.DecimalField(max_digits=5, decimal_places= 4)
	date_added = models.DateField(auto_now=False, auto_now_add=False)
        product = model.ForeingKey('Producto')
