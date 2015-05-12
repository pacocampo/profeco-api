from django.db import models


# Create your models here.

class Super (models.Model):
	nombre_super = models.CharField(max_length= 100, verbose_name='nombre_del_super')


	def __unicode__(self):
		return self.categoria


class Local (models.Model):
	foreign_key_super = models.ForeignKey(Super, verbose_name='foreign_key_id')
	direccion = models.CharField(max_length=300, verbose_name='Presentacion')
	categoria = models.ForeignKey('Categorias')
        latitud = models.DecimalField(max_digits=3, decimal_places= 10)
	longitud = models.DecimalField(max_digits=3, decimal_places= 10)

	def __unicode__(self):
		return self.producto

class Precios (models.Model):
	foreign_key_local = models.ForeignKey('Local')
	precio = models.DecimalField(max_digits=5, decimal_places= 4)
	date_added = models.DateField(auto_now=False, auto_now_add=False)
