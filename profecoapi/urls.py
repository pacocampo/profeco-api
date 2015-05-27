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
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', api_views.ProductoViewList.as_view(), name="producto-list"),
    url(r'^categories/$', api_views.CategoriaViewList.as_view(), name="categoria-list"),
    url(r'^categories/(?P<pk>[0-9]+)/$', api_views.CategoriaViewDetail.as_view(), name="categoria-detail"),
    url(r'^supermercados/', api_views.SupermercadosViewList.as_view(), name="supermercados-list"),
    url(r'^locales/(?P<pk>[0-9]+)/$', api_views.LocalViewDetail.as_view(), name="locales-detail"),

#url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {
 #           'document_root': settings.MEDIA_ROOT,
  #      }),
    #url(r'^images/icons/), 
    #url(r'^testing/', api_views.Pruebas.as_view(), name="test-list"),
]
