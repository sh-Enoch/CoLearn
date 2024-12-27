from django.urls import path
from .views import all_courses, course, create_course


urlpatterns = [
    path('courses/', all_courses, name='courses'),
    path('course/<int:pk>', course, name="specific_course"),
    path('create/course', create_course, name="create_course"),
]