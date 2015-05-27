from django.shortcuts import render
from .models import Categoria
from django.views.generic import View
from django.http import HttpResponse

def image(request):
	return render(request, "image.html")
	


