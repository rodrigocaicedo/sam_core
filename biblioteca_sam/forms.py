from django.forms import ModelForm
from django import forms
from django.db import models
from biblioteca_sam.models import Book,Reader,Borrowing


class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['boo_title','boo_author','boo_edition','boo_language','boo_subject','boo_publishinghouse','boo_publication','boo_acquisition','boo_observation','boo_value']
        
class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields=['rea_id']
        
class Borrowingform(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields=['bor_id','bor_datebor','bor_datereturn','bor_datemax','bor_observation','boo','rea']