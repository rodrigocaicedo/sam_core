#!/usr/bin/env python
# -*- coding: utf-8 -*-

from general_sam.models import Periodo_Lectivo

from usuarios_sam.outlookservice import get_my_messages

from datetime import date, datetime

import pytz


def schoolyear(request):

	if request.session.has_key("schoolyear") and request.session.has_key("schoolyear_pk"):
		pass
	else:
		today = date.today()
		if Periodo_Lectivo.objects.filter(inicio__lte=today, fin__gte=today).exists():
			current_schoolyear = Periodo_Lectivo.objects.get(inicio__lte=today, fin__gte=today)
		else:
			current_schoolyear = Periodo_Lectivo.objects.filter(actual = True).order_by("inicio").last()
		request.session['schoolyear'] = u"{0} - {1}".format(current_schoolyear.inicio.strftime("%Y"), current_schoolyear.fin.strftime("%Y"))
		request.session['schoolyear_pk'] = current_schoolyear.pk

	return {'schoolyear':Periodo_Lectivo.objects.get(pk = request.session["schoolyear_pk"]),'schoolyears':Periodo_Lectivo.objects.all().order_by("pk")}


def messages(request):
	try:
		access_token = request.session["access_token"]
		messages = get_my_messages(access_token, request.user)
		for message in messages["value"]:
			datetime_string = message["receivedDateTime"]
			recibido = datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%SZ")
			utc = pytz.timezone("UTC")
			recibido = utc.localize(recibido)
			message["recibido"] = recibido

		return {"messages": messages}
	except:
		return {}