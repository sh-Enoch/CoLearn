from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Course, Modules, Lessons, Quizzes, CourseEnrollment
from .forms import *
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin   
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib import messages


class CourseListView(LoginRequiredMixin, ListView):
    """List all courses in the platform."""
    template_name = 'courses/course_list.html'
    model = Course
    context_object_name = 'courses'

class ModuleListView(LoginRequiredMixin, ListView):
    """List all modules in the platform."""
    template_name = 'courses/module_list.html'
    model = Modules
    context_object_name = 'modules'

class LessonListView(LoginRequiredMixin, ListView):
    """List all lessons in the platform."""
    template_name = 'courses/lesson_list.html'
    model = Lessons
    context_object_name = 'lessons'



class CourseDetailView(LoginRequiredMixin, DetailView):
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

    

class ModuleDetailView(LoginRequiredMixin, DetailView):
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

class LessonDetailView(LoginRequiredMixin, DetailView):
    """Defines a detailed view for a lesson."""
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'lesson'
    queryset = Lessons.objects.all()

    def get_context_data(self, **kwargs):
        """Get the context data for the lesson."""
        context = super().get_context_data(**kwargs)
        lesson_id = self.kwargs.get('pk')
        context['quiz'] = Quizzes.objects.filter(lesson_id=lesson_id)
        return context



class CourseCreateView(LoginRequiredMixin, CreateView):
    """Defines a way to add courses on to the courses available."""
    template_name = 'courses/course_create.html'
    form_class = CourseCreateForm

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')
    

class ModuleCreateView(LoginRequiredMixin, CreateView):
    """Defines a way to add modules on to the modules available."""
    template_name = 'courses/module_create.html'
    form_class = ModulesCreateForm
    context_object_name = 'module'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        course_id = self.kwargs.get('course_id')
        context['course_id'] = course_id
        return context
    
    def get_success_url(self):
        return reverse('module-detail', kwargs={'pk':self.object.id})
class LessonCreateView(LoginRequiredMixin, CreateView):
    template_name = 'courses/lesson_create.html'
    form_class = LessonsCreateForm
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        module_id = self.kwargs.get('module_id')
        print(f"Debug - Module ID: {module_id}")  # Debug line
        context['module_id'] = module_id
        return context

    def form_valid(self, form):
        module_id = self.kwargs.get('module_id')
        form.instance.module = Modules.objects.get(id=module_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('module-detail', kwargs={'pk': self.object.module.id})

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    """Defines a way to update courses."""
    template_name = 'courses/course_update.html'
    form_class = CourseCreateForm
    queryset = Course.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')
    

class ModuleUpdateView(LoginRequiredMixin, UpdateView):
    """Defines a way to update modules."""
    template_name = 'courses/module_update.html'
    form_class = CourseCreateForm
    queryset = Modules.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('module-list')
    

class LessonUpdateView(LoginRequiredMixin, UpdateView):
    """Defines a way to update lessons."""
    template_name = 'courses/lesson_update.html'
    form_class = CourseCreateForm
    queryset = Lessons.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('lesson-list')
    

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    """Defines a way to delete courses."""
    template_name = 'courses/course_delete.html'
    queryset = Course.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')

class ModuleDeleteView(LoginRequiredMixin, DeleteView):
    """Defines a way to delete modules."""
    template_name = 'courses/module_delete.html'
    context_object_name = 'module'
    queryset = Modules.objects.all()

    def get_queryset(self):
        context = super().get_queryset()
        course_id = self.object.course.id
        context['course_id'] = course_id
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.object.course.id
        context['course_id'] = course_id
        return context

    def get_success_url(self):
        """Redirect to the module list."""
        return reverse('module-list')

class LessonDeleteView(LoginRequiredMixin, DeleteView):
    """Defines a way to delete lessons."""
    template_name = 'courses/lesson_delete.html'
    queryset = Lessons.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('lesson-list')



class CourseUpdateView(LoginRequiredMixin, UpdateView):
    """Defines a way to update courses."""
    template_name = 'courses/course_update.html'
    form_class = CourseCreateForm
    queryset = Course.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')
    

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    """Defines a way to delete courses."""
    template_name = 'courses/course_delete.html'
    queryset = Course.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')



"""Handle Read create update and delete operations for the quizzes"""
class QuizzesCreateView(LoginRequiredMixin, CreateView):
    """Defines a way to add quizzes on to the quizzes available."""
    template_name = 'courses/quizzes_create.html'
    form_class = QuizzesCreateForm
    context_object_name = 'quiz'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        lesson_id = self.object.lesson.id
        context['lesson_id'] = lesson_id
        return context

    def get_success_url(self):
        """Redirect to the course list."""
    
        return  reverse('lesson-detail', kwargs={'pk':self.object.lesson.id})
    

class QuizzesUpdateView(LoginRequiredMixin, UpdateView):
    """Defines a way to update quizzes."""
    template_name = 'courses/quizzes_update.html'
    form_class = QuizzesCreateForm
    queryset = Quizzes.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('quizzes-list')
    

class QuizzesDeleteView(LoginRequiredMixin, DeleteView):
    """Defines a way to delete quizzes."""
    template_name = 'courses/quizzes_delete.html'
    context_object_name = 'quiz'
    queryset = Quizzes.objects.all()


    
    def get_context_data(self, **kwargs):
        """Get the context data for the quizzes."""

        context =  super().get_context_data(**kwargs)
        lesson_id = self.object.lesson.id
        context['lesson_id'] = lesson_id
        return context
    

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('lesson-detail', kwargs={'pk': self.object.lesson.id})
    

class QuizzesListView(LoginRequiredMixin, ListView):
    """List all quizzes in the platform."""
    template_name = 'courses/quizzes_list.html'
    model = Quizzes
    context_object_name = 'quizzes'


    def get_queryset(self):
         return Quizzes.objects.order_by( 'lesson') 
    
    def get_context_data(self, **kwargs): 
        """Get the context data for the quizzes.""" 
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all().prefetch_related('modules__lessons_set__quizzes_set')
        return context


class QuizzesDetailView(LoginRequiredMixin, DetailView):
    """Defines a detailed view for a quiz."""
    template_name = 'courses/quizzes_detail.html'
    context_object_name = 'quiz'
    queryset = Quizzes.objects.all()

    def get_context_data(self, **kwargs):
        """Get the context data for the quiz."""
        context = super().get_context_data(**kwargs)
        quiz = self.get_object()
        context['is_list'] = isinstance(quiz, list)
        context['lesson'] = quiz.lesson

        return context
    

class CourseEnrollmentView(LoginRequiredMixin, CreateView):
    """Defines a way to enroll in a course."""
    template_name = 'courses/course_enrollment.html'
    form_class = CourseEnrollmentForm

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')
    

class CourseEnrollmentUpdateView(LoginRequiredMixin, UpdateView):
    """Defines a way to update course enrollment."""
    template_name = 'courses/course_enrollment_update.html'
    form_class = CourseEnrollmentForm
    queryset = CourseEnrollment.objects.all()

    def get_success_url(self):
        """Redirect to the course list."""
        return  reverse('course-list')
    

class CourseEnrollmentDeleteView(LoginRequiredMixin, DeleteView):
    """Defines a way to delete course enrollment."""
    template_name = 'courses/course_enrollment_delete.html'
    queryset = CourseEnrollment.objects.all()

    def get_success_url(self):

        """Redirect to the course list."""
        return  reverse('course-list')
    

class CourseEnrollmentListView(LoginRequiredMixin, ListView):
    """List all course enrollments in the platform."""
    template_name = 'courses/course_enrollment_list.html'
    model = CourseEnrollment
    context_object_name = 'enrollment'


class CourseEnrollmentDetailView(LoginRequiredMixin, DetailView):
    """Defines a detailed view for a course enrollment."""
    template_name = 'courses/course_enrollment_detail.html'
    context_object_name = 'enrollment'
    queryset = CourseEnrollment.objects.all()

    def get_context_data(self, **kwargs):
        """Get the context data for the course enrollment."""
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs.get('pk') 
        context['student'] = CourseEnrollment.objects.filter(course_id=course_id) 
        return context


class EnrollinCourse(LoginRequiredMixin, View):
    """Enroll in a course."""
    def get(self, request, *args, **kwargs):
        """Display the enrollment form."""
        course = get_object_or_404(Course, id=kwargs['pk'])
        form = CourseEnrollmentForm(initial={'course': course})
        return render(request, 'courses/course_enrollment.html', {'form': form})                                   

    def post(self, request, *args, **kwargs):
        """Enroll in a course."""
        course = get_object_or_404(Course, id=kwargs['pk'])

        # Check if the user is already enrolled in the course
        if CourseEnrollment.objects.filter(student=request.user, course=course).exists():
            messages.warning(request, f"You are already enrolled in {course.title}.")
            return redirect('course-detail', pk=course.id)
        
        CourseEnrollment.objects.create(student=request.user, course=course)
        messages.success(request, f"Successfully enrolled in {course.title}!")

        return redirect('course-detail', pk=course.id)