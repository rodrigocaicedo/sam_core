from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from capellania_sam import views

urlpatterns = [
#    url(r'^$',views.index, name='index'),
    url(r'^informe1/$',views.CreateInformeGeneral, name='nuevo_informe1'),


]
urlpatterns += staticfiles_urlpatterns()
