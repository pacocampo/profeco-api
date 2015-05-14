from django.shortcuts import render
from profeco.models import Categoria, Producto
from supermercado.models import Precio, Local, Supermercado
from django.http import Http404
from .serializers import CategoriaSerializer, ProductoSerializer, PreciosSuperSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CategoriaViewList(APIView):

	def get (self, request, format=None):
		categorias = Categoria.objects.all()
		serializer = CategoriaSerializer(categorias, many= True)
		return Response(serializer.data)

class ProductoViewList(APIView):

	def get (self, request, format=None):
		productos = Producto.objects.all()
		serializer = ProductoSerializer(productos, many= True)
		return Response(serializer.data)


class SupermercadosViewList(APIView):

	def get (self, request, format=None):
		precios = Precio.objects.all()
		serializer = PreciosSuperSerializer(precios, many= True)
		return Response(serializer.data)




# Create your views here.
