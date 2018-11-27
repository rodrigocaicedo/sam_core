from django.contrib import admin
from biblioteca_sam.models import Reader,Book,Borrowing

# Register your models here.
admin.site.register(Reader)
admin.site.register(Book)
admin.site.register(Borrowing)