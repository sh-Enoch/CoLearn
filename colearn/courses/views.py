from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Course, Modules, Lessons
from .forms import CourseCreateForm, LessonsCreateForm, ModulesCreateForm
from django.shortcuts import redirect, reverse



class CourseListView(ListView):
    """List all courses in the platform."""
    template_name = 'courses/course_list.html'
    model = Course
    context_object_name = 'courses'

class ModuleListView(ListView):
    """List all modules in the platform."""
    template_name = 'courses/module_list.html'
    model = Modules
    context_object_name = 'modules'

class LessonListView(ListView):
    """List all lessons in the platform."""
    template_name = 'courses/lesson_list.html'
    model = Lessons
    context_object_name = 'lessons'



class CourseDetailView(DetailView):
    """Defines a detailed view for a course."""
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    queryset = Course.objects.all()

    def get_context_data(self, **kwargs):
        """Get the context data for the course."""
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs.get('pk') 
        context['module'] = Modules.objects.filter(course_id=course_id) 
        return context


class ModuleDetailView(DetailView):
    """Defines a detailed view for a module."""
    template_name = 'courses/module_detail.html'
    context_object_name = 'module'
    queryset = Modules.objects.all()

    def get_context_data(self, **kwargs):
        """Get the context data for the module."""
        context = super().get_context_data(**kwargs)
        module_id = self.kwargs.get('pk')
        context['lesson'] = Lessons.objects.filter(module_id=module_id)
        return context

class LessonDetailView(DetailView):
    """Defines a detailed view for a lesson."""
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'lesson'
    queryset = Lessons.objects.all()



class CourseCreateView(CreateView):
    """Defines a way to add courses on to the courses available."""
    template_name = 'courses/course_create.html'
    form_class = CourseCreateForm

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')
    

class ModuleCreateView(CreateView):
    """Defines a way to add modules on to the modules available."""
    template_name = 'courses/module_create.html'
    form_class = ModulesCreateForm

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('module-list')
    

class LessonCreateView(CreateView):
    """Defines a way to add lessons on to the lessons available."""
    template_name = 'courses/lesson_create.html'
    form_class = LessonsCreateForm

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('lesson-list')
    



class CourseUpdateView(UpdateView):
    """Defines a way to update courses."""
    template_name = 'courses/course_update.html'
    form_class = CourseCreateForm
    queryset = Course.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')
    

class ModuleUpdateView(UpdateView):
    """Defines a way to update modules."""
    template_name = 'courses/module_update.html'
    form_class = CourseCreateForm
    queryset = Modules.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('module-list')
    

class LessonUpdateView(UpdateView):
    """Defines a way to update lessons."""
    template_name = 'courses/lesson_update.html'
    form_class = CourseCreateForm
    queryset = Lessons.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('lesson-list')
    

class CourseDeleteView(DeleteView):
    """Defines a way to delete courses."""
    template_name = 'courses/course_delete.html'
    queryset = Course.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')

class ModuleDeleteView(DeleteView):
    """Defines a way to delete modules."""
    template_name = 'courses/module_delete.html'
    queryset = Modules.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('module-list')
    

class LessonDeleteView(DeleteView):
    """Defines a way to delete lessons."""
    template_name = 'courses/lesson_delete.html'
    queryset = Lessons.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('lesson-list')



class CourseUpdateView(UpdateView):
    """Defines a way to update courses."""
    template_name = 'courses/course_update.html'
    form_class = CourseCreateForm
    queryset = Course.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')
    

class CourseDeleteView(DeleteView):
    """Defines a way to delete courses."""
    template_name = 'courses/course_delete.html'
    queryset = Course.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')
