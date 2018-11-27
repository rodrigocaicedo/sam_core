
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from socioeco_sam import views

urlpatterns = [
    

    url(r'^nuevo_pedido/$', views.Nuevo_Pedido, name = 'nuevo_pedido'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/$',views.Resumen, name='resumen'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/motivo/$',views.Finalizar, name='finalizar'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/terminar/$',views.Terminar, name='temrinar'),    
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/confirmar/$',views.Confirmar, name='confirmar'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/motivo/editar/$$',views.Editar_Finalizar, name='editar_finalizar'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/representante/$',views.Registrar_Representante, name='representante'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/representante/(?P<representante_pk>[0-9A-Fa-f-]+)/editar/$',views.Editar_Representante, name='editar_representante'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/representante/(?P<representante_pk>[0-9A-Fa-f-]+)/eliminar/$',views.Eliminar_Representante, name='eliminar_representante'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/estudiante/$',views.Registrar_Estudiante, name='estudiante'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/estudiante/(?P<estudiante_pk>[0-9A-Fa-f-]+)/editar/$',views.Editar_Estudiante, name='editar_estudiante'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/estudiante/(?P<estudiante_pk>[0-9A-Fa-f-]+)/eliminar/$',views.Eliminar_Estudiante, name='eliminar_estudiante'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/domicilio/$',views.Registrar_Domicilio, name='domicilio'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/domicilio/(?P<domicilio_pk>[0-9A-Fa-f-]+)/editar/$',views.Editar_Domicilio, name='editar_domicilio'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/integrante/$',views.Registrar_Integrante, name='integrante'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/integrante/(?P<integrante_pk>[0-9A-Fa-f-]+)/editar/$',views.Editar_Integrante, name='editar_integrante'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/integrante/(?P<integrante_pk>[0-9A-Fa-f-]+)/eliminar/$',views.Eliminar_Integrante, name='eliminar_integrante'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/situacion_habitacional/$',views.Registrar_Situacion_Habitacional, name='situacion'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/situacion_habitacional/(?P<situacion_pk>[0-9A-Fa-f-]+)/editar/$',views.Editar_Situacion_Habitacional, name='editar_situacion'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/responsable_gastos/$',views.Registrar_Responsable_Gastos, name='responsable'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/responsable_gastos/(?P<responsable_pk>[0-9A-Fa-f-]+)/editar/$',views.Editar_Responsable_Gastos, name='editar_responsable'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/propiedades/$',views.Registrar_Propiedades, name='propiedades'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/propiedades/(?P<propiedades_pk>[0-9A-Fa-f-]+)/editar/$',views.Editar_Propiedades, name='editar_propiedades'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/ingresos/$',views.Registrar_Ingresos, name='ingresos'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/ingresos/(?P<ingresos_pk>[0-9A-Fa-f-]+)/editar/$',views.Editar_Ingresos, name='editar_ingresos'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/gastos/$',views.Registrar_Gastos, name='gastos'),
    url(r'^(?P<pedido_pk>[0-9A-Fa-f-]+)/gastos/(?P<gastos_pk>[0-9A-Fa-f-]+)/editar/$',views.Editar_Gastos, name='editar_gastos'),
    url(r'^enviados/$', views.Enviados, name = 'enviados'),
    url(r'^enviados/(?P<pedido_pk>[0-9A-Fa-f-]+)/$', views.Detalle_Enviado, name = 'detalle_enviado'),
    url(r'^enviados/reporte/$', views.Exportar_Enviados_Xls, name = 'exportar_enviados_xls'),
    url(r'^enviados/reporte/estadogeneral/$', views.Exportar_Resumen_Xls, name = 'exportar_enviados_xls'),
    url(r'^enviados/reporte/estadorequeridos/$', views.Exportar_Resumen_Req_Xls, name = 'exportar_enviados_xls'),
    url(r'^enviados/reporte/estadonorequeridos/$', views.Exportar_Resumen_No_Req_Xls, name = 'exportar_enviados_xls'),
    url(r'^enviados/reporte/estudiantesresumen/$', views.Exportar_Est_1718_Resumen, name = 'exportar_estudiantes_resumen_xls'),
    url(r'^enviados/reporte/matriculadoscompleto/$', views.Exportar_Enviados_Matriculados_Xls, name = 'exportar_estudiantes_enviados_xls'),  
    url(r'^enviados/reporte/admisiones/$', views.Exportar_Admisiones_Xls, name = 'exportar_admisiones'),
    #Exportar_Admisiones_Xls
    #url(r'^profesores/(?P<id_asignacion>\d+)/$',views.message, name='profesor'),
    #url(r'^dece/$',views.message_dece, name='message_dece'),
    #url(r'^pastoral/$',views.message_cape, name='message_cape'),
    #url(r'^psicologia/$',views.message_psico, name='message_psico'),
    #url(r'^disciplina/$',views.message_disci, name='message_disci'),
    #url(r'^extracurriculares/$',views.message_extras, name='message_extras'),
    #url(r'^transporte/$',views.message_trans, name='message_trans'),


]
urlpatterns += staticfiles_urlpatterns()
