from .models import Enrollment, Module, Course
from django.forms import forms
from django.forms import ModelForm


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor']