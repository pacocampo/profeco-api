from django.db import models
from profeco.models import Producto

# Create your models here.

class Supermercado (models.Model):
	nombre_super = models.CharField(max_length= 100, verbose_name='nombre_del_super')


	def __unicode__(self):
		return self.nombre_super


class Local (models.Model):
	tienda = models.ForeignKey('Supermercado', related_name='tienda', null=True)
	direccion = models.CharField(max_length=300, verbose_name='direccion')
	latitud = models.DecimalField(max_digits=13, decimal_places= 10)
	longitud = models.DecimalField(max_digits=13, decimal_places= 10)

	def __unicode__(self):
		return self.tienda


class Precio (models.Model):
	local = models.ForeignKey('Local', related_name='local')
	precio = models.DecimalField(max_digits=5, decimal_places= 4,)
	date_added = models.DateField(auto_now=False, auto_now_add=False)
        producto = models.ForeignKey(Producto, related_name='productokey')
