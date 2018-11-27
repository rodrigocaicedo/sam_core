from django.contrib import admin
from capellania_sam.models import InformeGeneral, InformeRemision, InformeNovedades, InformeSeguimiento, ControlDeFormulario, Profesor, Estudiante, Capellan

admin.site.register(InformeGeneral)
admin.site.register(InformeRemision)
admin.site.register(InformeNovedades)
admin.site.register(InformeSeguimiento)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Capellan)
# Register your models here.
