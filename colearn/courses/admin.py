from django.contrib import admin
from .models import Course,  Modules, Lessons

# Register your models here.

admin.site.register(Course)
admin.site.register(Modules)
admin.site.register(Lessons)
