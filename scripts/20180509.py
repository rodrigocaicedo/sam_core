from usuarios_sam.models import Student, Students, Relative, People, Student_Relative, CustomUser as User
usuarios = User.objects.all()
for user in usuarios:
  if not user.first_name == user.first_name.title():
    user.first_name = user.first_name.title()
    user.father_last_name = user.father_last_name.title()
    user.mother_last_name = user.mother_last_name.title()
    user.save()
estudiantes = Students.objects.all()
for x in estudiantes:
  defaults = {"joined":x.id_students.date_joined}
  if "student.montebelloacademy.org" in x.id_students.email:
    defaults["state"] = "Aceptado"
    defaults["through"] = "Admisiones"
  else:
    defaults["state"] = "Matriculado"
    defaults["through"] = "Migracion Inicial"
  student, created = Student.objects.get_or_create(user = x.id_students, defaults= defaults)
  if created == True:
    print student
  if x.id_father:
    relative_father, created = Relative.objects.get_or_create(user = x.id_father, defaults={'alive':True})
    if created == True:
      print relative_father
    defaults={'relationship':"father", 'live_together': True, 'withdraw' : True, 'notifications' : True}
    if x.id_tutor == x.id_father:
      defaults['legal_representative'] = True

    father_bond, created = Student_Relative.objects.get_or_create(student = student, relative = relative_father, defaults = defaults)
    if created == True:
      print father_bond
  if x.id_mother:
    relative_mother, created = Relative.objects.get_or_create(user = x.id_mother, defaults={'alive':True})
    if created == True:
      print relative_mother
    defaults={'relationship':'mother', 'live_together':True, 'withdraw':True, 'notifications':True}
    if x.id_tutor == x.id_mother:
      defaults['legal_representative'] = True
    mother_bond, created = Student_Relative.objects.get_or_create(student = student, relative = relative_mother, defaults = defaults)
    if created == True:
      print mother_bond
  relative_tutor, created = Relative.objects.get_or_create(user = x.id_tutor, defaults={'alive':True})
  if created == True:
    print relative_tutor
  defaults = {'relationship':'other', 'live_together':True, 'withdraw':True, 'notifications':True, 'legal_representative':True}
  tutor_bond, created = Student_Relative.objects.get_or_create(student = student, relative = relative_tutor, defaults = defaults)
  if created == True:
    print tutor_bond
  #for relation in x.id_students.student.student_relative_set.all():
  #  print relation  