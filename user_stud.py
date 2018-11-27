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


from usuarios_sam.models import CustomUser as User
import csv

with open('user_stud.csv') as file:
    reader = csv.reader(file)
    for x in reader:
        nombres = x[0]
        materno = x[2]
        paterno = x[1]
        id = x[3]
        email = x[4]
        genero = x[5]
        telefono = x[6]
        try:
            usuario = User.objects.get(email = email)
            usuario.identity = id
            usuario.first_name = nombres
            usuario.father_last_name = paterno
            usuario.mother_last_name = materno
            usuario.gender = genero[0]
            usuario.phone = telefono
            usuario.save()
        except:
            print email
            User.objects.create(email = email, identity = id, first_name = nombres, father_last_name = paterno, mother_last_name = materno, gender = genero[0], phone = telefono)
