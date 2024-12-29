from django.contrib import admin

# Register your models here.
from .models import StudentUser, InstructorUser

admin.site.register(StudentUser)
admin.site.register(InstructorUser)
