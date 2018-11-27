#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

proj_path = "/var/www/django_projects/sam/"
# This is so Django knows where to find sstuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sam.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from usuarios_sam.models import CustomUser as User, Students

from general_sam.models import Matricula, Clase
import csv

with open('matricula.csv') as file:
    tutor = User.objects.get(email = "rodrigo@montebelloacademy.org")
    reader = csv.reader(file)
    for x in reader:
        email = x[0]
        paralelo = x[2]
        clase = x[1]
        print email
        print clase, paralelo
        clase = Clase.objects.get(nivel__nombre = clase, paralelo = paralelo)
        try:
            usuario = User.objects.get(email = email)
            estudiante = Students.objects.create(id_students = usuario, id_tutor = tutor)

        except:
            estudiante = Students.objects.get(id_students__email = email)

        Matricula.objects.create(estudiante = estudiante, clase = clase, tipo = "OR")
