from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from usuarios_sam import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^login/$',views.login_view, name='login'),
    url(r'^consent/$',views.login_view_app, name='login_view_app'),
    url(r'^logout/$',views.logout_view, name='salida'),
    url(r'^(?P<usuario_id>\d+)/$',views.profile_view, name = "perfil"),
	url(r'^gettoken/$', views.gettoken, name='gettoken'),
	url(r'^gettokenapp/$', views.gettokenapp, name='gettokenapp'),
]
urlpatterns += staticfiles_urlpatterns()
