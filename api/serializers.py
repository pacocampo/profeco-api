from profeco.models import Categoria, Producto
from rest_framework import serializers
from supermercado.models import Local, Precio, Supermercado, Producto

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = ('categoria', 'imagen')

class ProductoSerializer(serializers.ModelSerializer):
	categoria = serializers.StringRelatedField()

	class Meta:
		model = Producto
		fields = ('producto','marca', 'descripcion', 'presentacion', 'categoria')


class PreciosSuperSerializer(serializers.ModelSerializer):
	local  = serializers.StringRelatedField()
	precio  = serializers.StringRelatedField()

        class Meta:
	        model = Precio
                fields = ('local','precio', 'producto-key')
