from .models  import Course, Modules, Lessons
from django import forms


class CourseCreateForm(forms.ModelForm):
    """Form for creating a course."""
    class Meta:
        model = Course
        fields = ['title', 'description', 'summary', 'featured', 'creator']




        