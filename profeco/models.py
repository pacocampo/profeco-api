from django.db import models

# Create your models here.
class Categoria (models.Model):
	categoria = models.CharField(max_length= 100, verbose_name='Categoria')
	imagen = models.ImageField(max_length = 350, verbose_name='Imagen')

	def __unicode__(self):
		return self.categoria

class Producto (models.Model):
	producto = models.CharField(max_length =  200, verbose_name='Producto')
	marca = models.CharField(max_length = 100, verbose_name='Marca')
	descripcion = models.CharField(max_length = 250, verbose_name='Descripcion')
	presentacion = models.CharField(max_length=300, verbose_name='Presentacion')
	categoria = models.ForeignKey('Categoria')

	def __unicode__(self):
		return self.producto

class PrecioProfeco (models.Model):
	producto = models.ForeignKey('Producto')
	precio_min = models.DecimalField(max_digits=5, decimal_places= 4)
	precio_max = models.DecimalField(max_digits=5, decimal_places= 4)
	precio_prom = models.DecimalField(max_digits=5, decimal_places= 4)
	date_added = models.DateField(auto_now=False, auto_now_add=False)
