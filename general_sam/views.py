from django.shortcuts import render, redirect, render_to_response
from general_sam.models import Matricula, Periodo_Lectivo
from usuarios_sam.models import Students, CustomUser

from usuarios_sam.forms import StudentForm


# Create your views here.

def Mantenimiento(request):
	return render_to_response("general_sam/mantenimiento.html")

def NoUrl(request):
	return render_to_response("general_sam/no_url.html")

def Info_Estudiante(request, estudiante_id):
	try:
		estudiante = Matricula.objects.get(estudiante__pk = estudiante_id)
	except:
		return redirect(Lista_Estudiantes)
	if request.method =="POST":
		form = StudentForm(request.POST, instance = estudiante)
		if form.is_valid():
			form.save()
			return redirect(Lista_Estudiantes)

	else:
		form = StudentForm(instance = estudiante)

		return render(request, "",{"form":form})

def Lista_Estudiantes(request):
	periodo_lectivo = Periodo_Lectivo.objects.get(actual = True)
	estudiantes = Matricula.objects.filter(periodo_lectivo = periodo_lectivo)
	return render(request, "", {"estudiantes":estudiantes})





