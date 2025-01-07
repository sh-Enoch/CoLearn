from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course, CourseEnrollment, Modules, Lessons
# Create your views here.


def get_statistics():
    """Method to get the course statistics."""
    courses =  Course.objects.all()
    course_count = courses.count()

    modules =  Modules.objects.order_by(courses)





class ProfileView(TemplateView):
    template_name = 'profile/profile.html'
