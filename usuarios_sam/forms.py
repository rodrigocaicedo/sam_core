
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from usuarios_sam.models import CustomUser, Students

from django import forms

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """


    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ('first_name','father_last_name','mother_last_name', "user_photo")

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        """del self.fields['username']"""

    class Meta:
        model = CustomUser
        fields = ('first_name','father_last_name','mother_last_name', "user_photo")

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        exclude = []