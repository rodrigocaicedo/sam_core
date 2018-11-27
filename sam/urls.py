"""sam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import capellania_sam, usuarios_sam,admisiones_sam, tinymce, secretaria_sam,uniformes_sam,biblioteca_sam, canales_sam, socioeco_sam

from general_sam import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^informes/', include("capellania_sam.urls")),
    url(r'^user/', include("usuarios_sam.urls", namespace="usuarios_sam")),
    url(r'^canales/', include("canales_sam.urls")), 
    url(r'^admisiones/', include("admisiones_sam.urls")),
    url(r'^comunicaciones/', include("comunicaciones_sam.urls")),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^secretaria/', include('secretaria_sam.urls')),
    url(r'^uniformes/', include('uniformes_sam.urls')),
    url(r'^biblioteca/', include('biblioteca_sam.urls')),
    url(r'^personal/', include('personal_sam.urls')),
    url(r'^facturas/', include('facturacion_sam.urls')),
    url(r'^socioeconomico/', include('socioeco_sam.urls')),    
    #url(r'^', views.Mantenimiento, name='mantenimiento,'),
    #url(r'^', views.NoUrl, name='nourl,'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


