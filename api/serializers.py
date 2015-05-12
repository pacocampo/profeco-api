from profeco.models import Categoria, Producto
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Categoria
		fields = ('categoria', 'imagen')

class ProductoSerializer(serializers.ModelSerializer):
	categoria = serializers.StringRelatedField()

	class Meta:
		model = Producto
		fields = ('producto','marca', 'descripcion', 'presentacion', 'categoria')

