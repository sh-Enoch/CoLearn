from .models import StudentUser, InstructorUser
from django.forms import ModelForm


class StudentUserForm(ModelForm):
    """Form for the StudentUser model"""
    class Meta:
        model = StudentUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'instructor']
        