from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from usuarios_sam.models import CustomUser, CustomUserManager, Students, People,Tutor,Teacher, RelationshipStudent, Student, Relative, Student_Relative, Relative_Details

from usuarios_sam.forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('identity','first_name', 'father_last_name', 'mother_last_name','preferred_name','birthdate','gender','birth_country', 'country_home', 'user_photo')}),
        (_('Contact info'), {'fields': ('phone', 'cell', 'address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','father_last_name', 'mother_last_name','password1', 'password2', 'user_photo')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'first_name', 'father_last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'father_last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Students)
admin.site.register(People)
admin.site.register(Tutor)
admin.site.register(Teacher)
admin.site.register(RelationshipStudent)
admin.site.register(Student)
admin.site.register(Relative)
admin.site.register(Relative_Details)
admin.site.register(Student_Relative)

# Register your models here.
