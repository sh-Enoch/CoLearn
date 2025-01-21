from django.contrib import admin

# Register your models here.
from .models import StudentUser, InstructorUser, User, Profile

admin.site.register(StudentUser)
admin.site.register(InstructorUser)
admin.site.register(User)
admin.site.register(Profile)
