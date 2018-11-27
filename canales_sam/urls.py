
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from canales_sam import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^grupos/$',views.list_levels, name='niveles'),
    url(r'^grupos/(?P<id_grupo>\d+)/$',views.level, name='nivel'),
    url(r'^departamentos/$',views.list_department, name='lista_departamento'),    
    url(r'^departamentos/(?P<id_departamento>\d+)/$',views.message_department, name='mensaje_departamento'),
    url(r'^profesores/(?P<id_asignacion>\d+)/$',views.message, name='profesor'),
    url(r'^dece/$',views.message_dece, name='message_dece'),
    url(r'^pastoral/$',views.message_cape, name='message_cape'),
    url(r'^psicologia/$',views.message_psico, name='message_psico'),
    url(r'^disciplina/$',views.message_disci, name='message_disci'),
    url(r'^extracurriculares/$',views.message_extras, name='message_extras'),
    url(r'^transporte/$',views.message_trans, name='message_trans'),
    url(r'^temas/$',views.list_topics, name='lista_temas'),    
    url(r'^temas/(?P<id_tema>\d+)/$',views.message_topics, name='mensaje_temas'),    
    #url(r'^periodo_lectivo$', views.activacion_periodo_lectivo, name='activacion_periodo_lectivo,'),
    #url(r'^matriculas$', views.matriculacion_individual, name='matriculacion_individual,'),
    #url(r'^clases$', views.lista_clases, name='lista_clases,'),
    #url(r'^clases/(?P<clase_id>\d+)/$', views.detalle_clase, name='detalle_clase,'),
    #url(r'^estudiantes$', views.lista_estudiantes, name='lista_estudiantes,'),
    #url(r'^estudiantes/(?P<estudiante_id>\d+)/$', views.detalle_estudiante, name='detalle_estudiante,'),	
    #url(r'^enviar/(?P<info>\d+)/(?P<comunicacion>\d+)/$',views.Send_Email_Applicant, name='Correo'),
    #url(r'^clear$', views.clear_sent_messages, name='clear_sent_messages'),
    #url(r'^$', views.run_mail_job, name='run_mail_job'),

]
urlpatterns += staticfiles_urlpatterns()
