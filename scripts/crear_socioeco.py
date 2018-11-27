# -*- coding: utf-8 -*-

import csv
from socioeco_sam.models import Evaluacion_Socioeco

from datetime import datetime

from general_sam.models import Clase

from django.db import IntegrityError

with open("scripts/solicitudes.csv") as file:
	reader = csv.reader(file, delimiter = ";")
	for row in reader:
		representantes = []
		nombre = row[21].decode("utf-8")
		nombre = u"{0}".format(nombre)
		apellidos = row[22].decode("utf-8")
		apellidos = u"{0}".format(apellidos)
		nivel = u"{0}".format(row[19].decode("utf-8"))
		paralelo = row[20]
		pais = row[18]
		ciudad = u"{0}".format(row[17].decode("utf-8"))
		genero = row[16]
		fecha = row[15]
		fecha = datetime.strptime(fecha, "%d/%m/%Y")

		numero_id = row[2]
		correos = []
		familia = row[4]
		vive = row[5]
		clase = Clase.objects.get(nivel__nombre = nivel, paralelo = paralelo)
		if vive == "PADRES":
			solicitante = row[6].decode("utf-8")
			solicitante = u"{0}".format(solicitante)
			print solicitante, "Prueba"
			try:
				evaluacion, created = Evaluacion_Socioeco.objects.get_or_create(requerido = True, familia = row[4], defaults={"email": row[7], "solicitante":solicitante})

				print evaluacion, created

				evaluacion.estudiante_set.create(nombres = nombre, apellido_paterno = apellidos, 
					numero_id = numero_id, genero = genero, fecha_nacimiento = fecha,
					ciudad_nacimiento = ciudad, pais_nacimiento = pais, nivel = clase)
				evaluacion.integrante_familia_set.create(nombres_completos = u"{0} {1}".format(nombre, apellidos), fecha_nacimiento = fecha, numero_id = numero_id, estado_civil = "SOLTERO",
					parentesco = "HIJO", nivel_estudios = "BASICA", actividad = "Estudiante")
				evaluacion.motivo_solicitud = "Renovación de Convenio"
				evaluacion.capacidad_pago = 0
				evaluacion.save()
			except IntegrityError:
				pass
			except Evaluacion_Socioeco.MultipleObjectsReturned:
				pass

		else:
			lista_representantes = [6,8,10,12]
			
			for x in lista_representantes:
				representante = row[x].decode("utf-8")
				representante = u"{0}".format(representante)
				correo = row[x+1]
				print representante, "Prueba"
				if not representante or not correo:
					pass
				else:
					try:
						evaluacion, created = Evaluacion_Socioeco.objects.get_or_create(email = correo, requerido = True, defaults={"solicitante": representante, "familia": row[4]})
						print evaluacion, created
						try:
							evaluacion.estudiante_set.create(nombres = nombre, apellido_paterno = apellidos, 
								numero_id = numero_id, genero = genero, fecha_nacimiento = fecha,
								ciudad_nacimiento = ciudad, pais_nacimiento = pais, nivel = clase)
							evaluacion.integrante_familia_set.create(nombres_completos = u"{0} {1}".format(nombre, apellidos), fecha_nacimiento = fecha, numero_id = numero_id, estado_civil = "SOLTERO",
								parentesco = "HIJO", nivel_estudios = "BASICA", actividad = "Estudiante")
							evaluacion.motivo_solicitud = "Renovación de Convenio"
							evaluacion.capacidad_pago = 0
							evaluacion.save()
						except:
							pass
					except IntegrityError:
						pass