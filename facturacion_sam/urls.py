from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from facturacion_sam import views

urlpatterns = [
   
    #Facturas
    url(r'^CreaFacturas/(?P<email_s>\d+)/$',views.invoice_new, name='CreaFacturas'), 
  
]
urlpatterns += staticfiles_urlpatterns()
