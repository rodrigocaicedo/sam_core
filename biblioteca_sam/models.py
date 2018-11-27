from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Reader(models.Model):
    rea_id= models.AutoField(primary_key = True)
    rea_name= models.CharField(max_length = 150)
    
    def __unicode__(self):
        return self.rea_id

class Book(models.Model):
    boo_id = models.AutoField(primary_key = True)
    boo_title = models.CharField(max_length = 80)
    boo_author = models.CharField(max_length = 50)
    boo_edition = models.CharField(max_length = 30,blank = True)
    boo_language = models.CharField(max_length = 15)
    boo_subject = models.CharField(max_length = 50,blank = True)
    boo_publishinghouse = models.CharField(max_length = 20,blank = True)
    boo_publication = models.DateField(null=True,blank=True)
    boo_acquisition = models.DateField(null=True,blank=True)
    boo_observation = models.CharField(max_length = 80,blank = True)
    boo_value = models.IntegerField(blank = True)
    boo_state=models.BooleanField(default = True)

    def __unicode__(self):
        return self.boo_title

class Borrowing(models.Model):
    bor_id =  models.AutoField(primary_key = True)
    bor_datebor = models.DateField(null=True,blank=True)
    bor_datereturn = models.DateField(null=True,blank=True)
    bor_datemax = models.DateField(null=True,blank=True)
    bor_observation = models.CharField(max_length = 80,blank = True)
    boo = models.ForeignKey('Book')
    rea = models.ForeignKey('Reader')
    
    def __unicode__(self):
        return self.bor_datebor