#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from admisiones_sam.models import *


# Register your models here.

admin.site.register(Type_Tours)
admin.site.register(Forms)
admin.site.register(Applications)
admin.site.register(Quotas)
admin.site.register(Mails)
admin.site.register(Tours)
admin.site.register(Documents_Type)
#admin.site.register(Documents)
admin.site.register(Det_Documents)
admin.site.register(Type_Tests)
admin.site.register(Test)
admin.site.register(State_Applications)
admin.site.register(Reports_Tests)
admin.site.register(Invoices)
admin.site.register(Det_Reports)
admin.site.register(PeriodSchool)
admin.site.register(AccountingDepartment)
admin.site.register(AcademicSecretary)
admin.site.register(Type_Grade)
