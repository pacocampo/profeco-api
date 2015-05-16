
from django.shortcuts import render
from profeco.models import Categoria, Producto
from supermercado.models import Precio, Local, Supermercado
from django.http import Http404
from .serializers import CategoriaSerializer, ProductoSerializer, LocalSerializer, ProductSerializer, SuperSerializer, LocalsSerializer, PrecioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CategoriaViewList(APIView):

	def get (self, request, format=None):
		categorias = Categoria.objects.all()
		serializer = CategoriaSerializer(categorias, many= True)
		return Response(serializer.data)

class CategoriaViewDetail(APIView):
	def get_object(self, pk):
		try:
			return Producto.objects.filter(categoria = pk)
		except Producto.DoesNotExist:
			return Http404

	def get (self, request, pk, format=None):
		productos = self.get_object(pk)
		serializer = ProductSerializer(productos, many= True)
		return Response(serializer.data)

class SupermercadosViewList(APIView):

	def get (self, request, format=None):
		locales = Local.objects.all()
		serializer = LocalSerializer(locales, many=True)
		return Response(serializer.data)

class ProductoViewList(APIView):
	def get(self, request, format=None):
		productos = Producto.objects.all()
		serializer = ProductSerializer(productos, many= True)
		return Response(serializer.data)

class SuperViewList(APIView):
	def get(self, request, format=None):
		supers = Supermercado.objects.all()
		serializer = SuperSerializer(supers, many=True)
		return Response(serializer.data)

class PrecioViewList(APIView):
	def get(self, request, format=None):
		precios = Precio.objects.all()
		serializer = PrecioSerializer(precios, many=True)
		return Response(serializer.data)
