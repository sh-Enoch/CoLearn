from django.shortcuts import render
from courses.models import Course, Enrollment, Module
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CourseForm
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
# class courses(ListView):
#     model = Course
#     template_name = ""
#     context_object_name = "courses"



def all_courses(request):
    """function based view to list all courses for our user."""
    courses = Course.objects.all()
    context = {
        'courses':courses
    }

    return render(request, 'courses.html', context=context)

def course(request, pk):
    """Get a specific course."""
    course = Course.objects.get(id=pk)
    module = Module.objects.filter(course=course)

    context = {
        "course": course,
        "module":module
    }

    return render(request, 'course_specific.html', context=context)


def enroll_me(request, pk):
    """Let a user enroll to a given course on clicking the enroll button."""
    Enrollment.objects.create(
        student = '',
        course = '',
    )


#instructor
def create_modules(request):
    """Allow users to create modules for a course."""
    pass

#instructor

def create_course(request):
    """Allow users to create course."""
    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            course = form.save()

            course_html = render_to_string('partials/course_card.html', {'course':course})
            return JsonResponse({'success': True, 'course_html':course_html}, status=201)
        else:
            #render html errors

            error_html = render_to_string('partials/form_errors.html', {"form":form})
            return JsonResponse({"success": False, "error": error_html}, status=400)
        
    elif request.method == "GET":
        form = CourseForm()

        return render(request, 'add_course.html')


        

#instructor
def update_module(request, pk):
    """Update a given module in a course"""
    pass

def update_course(request, pk):
    """Allow users to update a given course."""
    pass


def delete_course(request, pk):
    """Allow users to delete the course they have created."""
    pass


def delete_module(request, pk):
    """Allow users to delete a given module."""
    pass



