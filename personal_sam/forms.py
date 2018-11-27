from django import forms
from django.db import models
from personal_sam.models import Type_Permissions,Permissions,Delegated_Activities,State_Permissions


class Permissionsform(forms.ModelForm):

    class Meta:
        model = Permissions
        fields = ['date' ,'applicant','date_initial','date_end','days','hours','reason']
   

   