from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from personal_sam import views

urlpatterns = [
   
    url(r'^postulaciones/$', views.Postulaciones_Personal, name="Postulaciones_Personal"),
    url(r'^Permisos/$', views.Permission, name='Permisos'),  
    url(r'^PreAprobacion/(?P<id>\d+)/$', views.PreApprove, name='PreAprobacion'),  
    url(r'^BuscarPreAprobacion/$', views.SearchPreApprove, name='BuscarPreAprobacion'), 
    url(r'^PermisosRRHH/$', views.Permission_rrhh, name='PermisosRRHH'),  
    url(r'^ListaTutores/$', views.ListTutors, name='ListaTutores'),    
]
urlpatterns += staticfiles_urlpatterns()
