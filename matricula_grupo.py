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

from general_sam.models import Matricula, Clase, Matricula_Grupo, Grupo
import csv

with open('matricula_grupo.csv') as file:
    tutor = User.objects.get(email = "rodrigo@montebelloacademy.org")
    reader = csv.reader(file)
    for x in reader:
        email = x[0]
        grupo = x[1]
        print email, grupo
        grupo = Grupo.objects.get(nombre = grupo)
        matricula = Matricula.objects.get(estudiante__id_students__email = email)
        print matricula, grupo
        Matricula_Grupo.objects.create(matricula = matricula, grupo = grupo)
