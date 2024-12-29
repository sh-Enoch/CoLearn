from django.shortcuts import render, reverse

# Create your views here.
from  django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import StudentUser, InstructorUser
from .forms import StudentUserForm


class StudentListView(ListView):
    """View for the list of students"""
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    queryset = StudentUser.objects.all()


class StudentCreateView(CreateView):
    """View for creating a new student"""
    template_name = 'students/create_student.html'
    form_class = StudentUserForm

    def get_success_url(self):
        return reverse('student-list')
    

class StudentUpdateView(UpdateView):
    """View for updating a student"""
    template_name = 'students/update_student.html'
    form_class = StudentUserForm
    queryset = StudentUser.objects.all()

    def get_success_url(self):
        return reverse('student-list')

class StudentDeleteView(DeleteView):
    """View for deleting a student"""
    template_name = 'students/delete_student.html'
    queryset = StudentUser.objects.all()

    def get_success_url(self):
        return reverse('student-list')
    
class StudentDetailView(DetailView):
    """View for viewing a student"""
    template_name = 'students/student_detail.html'
    queryset = StudentUser.objects.all()
    context_object_name = 'student'


