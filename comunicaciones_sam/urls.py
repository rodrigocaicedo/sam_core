from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from comunicaciones_sam import views

urlpatterns = [
    #url(r'^$',views.index, name='index'),
    url(r'^general$', views.Correo_General, name='correo_general'),
    url(r'^enviar/(?P<info>\d+)/(?P<comunicacion>\d+)/$',views.Send_Email_Applicant, name='Correo'),
    url(r'^clear$', views.clear_sent_messages, name='clear_sent_messages'),
    url(r'^envio_masivo$', views.run_mail_job, name='run_mail_job'),

]
urlpatterns += staticfiles_urlpatterns()
