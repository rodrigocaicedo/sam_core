#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from admisiones_sam.models import Applications, Type_Tours,Tours,PeriodSchool,State_Applications,Type_Tests,Test,Forms,Quotas,Invoices,Mails,Reports_Tests,Det_Reports,Documents_Type,Det_Documents,AccountingDepartment,Type_Grade
from usuarios_sam.models import CustomUser

class Applicationsnewform(forms.ModelForm):

    class Meta:
        model = Applications
        fields = ['id_applications','name_student','surname_student','gender_student','birth_date','birth_country','country_home','applied_grade','school_period','name_tutor' ,'surname_tutor','mail_tutor','phone_tutor','cell_tutor','name_school','address_school','last_year','special_observations','bank_code']
   
class ApplicationsChangeState(forms.ModelForm):

    class Meta:
        model = State_Applications 
        exclude=['id_state','initial_date' ,'final_date','id_applications',]
        
class TypeToursnewform(forms.ModelForm):

    class Meta:
        model = Type_Tours
        exclude = ['state','name_tour',]
       
class TypeToursEditform(forms.ModelForm):

    class Meta:
        model = Type_Tours
        exclude = ['name_tour',]
 

class TypeTestsnewform(forms.ModelForm):

    class Meta:
        model = Type_Tests
        fields=['date_test','date_test_pre','grade','teacher','time_test','time_test_pre','type_test','state']
       
class Testsnewform(forms.ModelForm):

    class Meta:
        model = Test
        exclude = ['id_applications','id_typetest'] 
        
       
class Toursnewform(forms.ModelForm):

    class Meta:
        model = Tours
        fields = ['id_tour','estado','id_typetour','id_applications']
        widgets = {'id_applications': forms.HiddenInput(),'estado': forms.HiddenInput()}
    
        
class Toursupdateform(forms.ModelForm):

    class Meta:
        model = Tours
        fields = ['id_tour','estado','id_typetour','id_applications']
        widgets = {'id_applications': forms.HiddenInput()}
        
        
class PeriodNewform(forms.ModelForm):

    class Meta:
        model = PeriodSchool
        exclude = ['per_id','per_state','per_name',]

class GradeNewform(forms.ModelForm):

    class Meta:
        model = Type_Grade
        fields=['id_typegrade','typegrade','typeschool']
       
class PeriodEditform(forms.ModelForm):

    class Meta:
        model = PeriodSchool
        exclude = ['per_id','per_name',]
        
class FormsNewform(forms.ModelForm):

    class Meta:
        model = Forms
        exclude=['date_form','id_applications',]

class CustomUserform(forms.ModelForm):

    class Meta:
        model = CustomUser
        exclude=['is_staff','is_active','is_superuser','date_joined','user_photo','password','groups','last_login','user_permissions',]
        
       
class QuotaNewform(forms.ModelForm):
    class Meta:
        model = Quotas
        fields = ['id_quotas','grade','max_students','old_students','available_students'] 
        
class InvoicesNewform(forms.ModelForm):
    class Meta:
        model = Invoices
        exclude = ['id_applications']

class MailsNewform(forms.ModelForm):

    class Meta:
        model = Mails
        fields = ['id_mails','title','sender','receiver','text','link']
        
class NewReportsTests(forms.ModelForm):
    
    class Meta:
        model=Reports_Tests
        exclude=['id_report','date_report','user','id_test','id_applications','id_typetest']

class NewDetReports(forms.ModelForm):
    class Meta:
        model=Det_Reports
        exclude=['id_detreport','id_report' ,'id_test', 'id_typetest','id_applications']
       

class NewDocuments_Type (forms.ModelForm):
    class Meta:
        model=Documents_Type
        fields = ['id_doctype','estado','grade','document'] 

class NewDetDocuments(forms.ModelForm):
    class Meta:
        model=Det_Documents
        fields=['id_doctype','file','state','id_applications']
        

class NewAccounting(forms.ModelForm):
    class Meta:
        model=AccountingDepartment
        exclude=['id_applications','id_accounting']
        
        
class ListTourForm(forms.Form):
    date_tour= forms.DateField(required=False)
    student = forms.CharField(required=False)
    grade = forms.CharField(required=False)
    tutor = forms.CharField(required=False)