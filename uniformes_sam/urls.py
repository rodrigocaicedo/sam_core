from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from uniformes_sam import views

urlpatterns = [
   #Inicio
   #url(r'^Inicio/$',views.Home, name='Inicio'), #pagina de inicio del sistema
   
    #Formulario
    url(r'^Proforma/$',views.Pedido, name='Proforma'), 
    
    #Consultas 
    url(r'^ListaRepresentantes/$', views.ListaTutor, name='ListaRepresentantes'),
]
urlpatterns += staticfiles_urlpatterns()