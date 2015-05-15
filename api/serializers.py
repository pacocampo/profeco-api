import django_filters
from profeco.models import Categoria, Producto
from rest_framework import serializers
from rest_framework import generics
from supermercado.models import Local, Precio, Supermercado

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = ('id', 'categoria', 'imagen')

class ProductoSerializer(serializers.ModelSerializer):
	categoria = serializers.StringRelatedField()

	class Meta:
		model = Producto
		fields = ('id', 'producto','marca', 'descripcion', 'presentacion', 'categoria')

class LocalSerializer(serializers.ModelSerializer):
	tienda = serializers.StringRelatedField()

	class Meta:
		model = Local
		fields = ('id','tienda', 'sucursal', 'latitud', 'longitud','tienda')


class PrecioSerializer(serializers.ModelSerializer):
	local = serializers.StringRelatedField()
	class Meta:
		model = Precio
		fields = ('precio', 'local')

class ProductSerializer(serializers.ModelSerializer):
	precios = PrecioSerializer(read_only=True, many=True)
	categoria = serializers.StringRelatedField()

	class Meta:
		model = Producto
		fields = ('id', 'producto', 'descripcion', 'marca', 'presentacion', 'categoria', 'precios')

class LocalsSerializer(serializers.ModelSerializer):
	locales = PrecioSerializer(read_only=True, many=True)

	class Meta:
		model = Local
		fields = ("id", "sucursal", "latitud", "longitud", "locales")


class SuperSerializer(serializers.ModelSerializer):
	supermercado = LocalsSerializer(read_only=True, many=True)

	class Meta:
		model = Supermercado
		fields = ('id', 'nombre_super', 'supermercado')



