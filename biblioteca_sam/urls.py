from django.conf.urls import include,url
from biblioteca_sam import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
   
    url(r'^nuevo/$', views.NewBook, name='nuevo'), #Nuevo registro de libros
	url(r'^consulta/$', views.search_book, name='consulta'), #consulta de libros
    url(r'^eliminar/(?P<boo_id>\d+)/$', views.delete_book, name='eliminar'),    #elimina el registro del libro solo si no esta prestado
    url(r'^editar/(?P<boo_id>\d+)/$', views.edit_book, name='editar'),  
    url(r'^registrar/(?P<boo_id>\d+)/$', views.register_book, name='registrar'),  # registra la salida o entrada de un libro a la biblioteca
    url(r'^Listalibros/$', views.ListBook, name='Listalibros'),
    url(r'^Listaautores/$', views.ListAuthor, name='Listaautores'),
]
urlpatterns += staticfiles_urlpatterns()

