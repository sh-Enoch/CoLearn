from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Course, Modules, Lessons
from .forms import CourseCreateForm
from django.shortcuts import redirect



class CourseListView(ListView):
    """List all courses in the platform."""
    template_name = 'courses/course_list.html'
    model = Course
    context_object_name = 'courses'



class CourseDetailView(DetailView):
    """Defines a detailed view for a course."""
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    queryset = Course.objects.all()



class CourseCreateView(CreateView):
    """Defines a way to add courses on to the courses available."""
    template_name = 'courses/course_create.html'
    form_class = CourseCreateForm

    def get_success_url(self):
        """Redirect to the course list."""
        return  redirect('course-list')




