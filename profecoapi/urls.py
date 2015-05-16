"""profecoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from api import views as api_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', api_views.ProductoViewList.as_view(), name="producto-list"),
    url(r'^categories/$', api_views.CategoriaViewList.as_view(), name="categoria-list"),
    url(r'^categories/(?P<pk>[0-9]+)/$', api_views.CategoriaViewDetail.as_view(), name="categoria-detail"),
    url(r'^supermercados/', api_views.SupermercadosViewList.as_view(), name="supermercados-list"),
    url(r'^testing/', api_views.PrecioViewList.as_view(), name="test-list"),
]
