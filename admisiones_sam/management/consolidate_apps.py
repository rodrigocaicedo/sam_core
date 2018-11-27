from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommmand):
	hostname = ''
	user = ''
	password = ''
	database = ''
	with open("/var/www/django_projects/last_imported_app","r+") as f:
	    last_code = f.read()
	import MySQLdb
	connection = MySQLdb.connect(host=hostname, user = user, passwd = password, db = database)
	cur = connection.cursor()
	query = "SELECT code, first_name_stap, name_stap, nacion_stap, residence_stap from studentsapp where code > {}".format(last_code)

	cur.execute(query)
	resultados = cur.fetchall()
	connection.close()
	for row in resultados:
	    print type(row)
	    print row[0], row[1], row[2], row[3], row[4]
	    with open("last_imported_app", "r+") as f:
	        id_code = u"{}".format(row[0])
	        print type(id_code)
	        f.write(id_code)

