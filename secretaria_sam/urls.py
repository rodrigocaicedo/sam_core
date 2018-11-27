from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from secretaria_sam import views

urlpatterns = [
    #url(r'^$',views.index, name='index'),
    url(r'^activar_periodo/(?P<periodo_lectivo>\d+)/$', views.activar_periodo, name = 'activar_periodo'),
    url(r'^periodo_lectivo$', views.activacion_periodo_lectivo, name='activacion_periodo_lectivo,'),

    #direcciones para matriculas
    url(r'^matriculas/$', views.matriculacion_individual, name='matriculacion_individual,'),
    url(r'^matriculas/activas/$', views.lista_matriculas, name='lista_matriculas,'),
    url(r'^matriculas/retirados/$', views.lista_matriculas_retirados, name='lista_matriculas_retirados,'),

    url(r'^matriculas/(?P<matricula_id>\d+)/retirar/$', views.retirar_matricula, name='retirar_matricula,'),    
    url(r'^matriculas/(?P<matricula_id>\d+)/reingresar/$', views.reingresar_matricula, name='reingresar_matricula,'),
    url(r'^matriculas/(?P<matricula_id>\d+)/editar/$', views.editar_matricula, name='editar_matricula,'),

    url(r'^matriculas/pedidos/(?P<apto_id>\d+)/$', views.pedido_matricula, name='pedido_matricula,'),
    url(r'^matriculas/pedidos/(?P<apto_id>\d+)/eliminar/$', views.eliminar_pedido_matricula, name='eliminar_pedido_matricula,'),

    url(r'^clases/$', views.lista_clases, name='lista_clases,'),
    url(r'^clases/(?P<clase_id>\d+)/$', views.detalle_clase, name='detalle_clase,'),
    url(r'^estudiantes/$', views.lista_estudiantes, name='lista_estudiantes,'),
    url(r'^estudiantes/(?P<estudiante_id>\d+)/$', views.detalle_estudiante, name='detalle_estudiante,'),    
    #url(r'^enviar/(?P<info>\d+)/(?P<comunicacion>\d+)/$',views.Send_Email_Applicant, name='Correo'),
    #url(r'^clear$', views.clear_sent_messages, name='clear_sent_messages'),
    #url(r'^$', views.run_mail_job, name='run_mail_job'),

]
urlpatterns += staticfiles_urlpatterns()
