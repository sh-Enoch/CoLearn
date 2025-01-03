
from django.contrib import admin
from .models import Course, Modules, Lessons, Quizzes, CourseEnrollment, Resource

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'created_at', 'featured']
    search_fields = ['title']

@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_filter = ['course']
    ordering = ['course', 'order']

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'order', 'duration']
    ordering = ['module', 'order']

@admin.register(Quizzes)
class QuizzesAdmin(admin.ModelAdmin):
    list_display = ['title', 'lesson', 'question']

@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'date_enrolled', 'progress', 'completed']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'lesson', 'file', 'link'] 
    list_filter = ['lesson']
    search_fields = ['title']
