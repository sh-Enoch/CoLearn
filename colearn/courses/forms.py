from .models  import Course, Modules, Lessons,  Quizzes, CourseEnrollment
from django import forms


class CourseCreateForm(forms.ModelForm):
    """Form for creating a course."""
    class Meta:
        model = Course
        fields = ['title', 'description', 'summary', 'featured', 'creator']


class ModulesCreateForm(forms.ModelForm):
    """Form for creating a module."""
    class Meta:
        model = Modules
        fields = ['course', 'title', 'description', 'order']



class LessonsCreateForm(forms.ModelForm):
    """Form for creating a lesson."""
    class Meta:
        model = Lessons
        fields = ['module', 'title', 'content', 'video_url', 'duration', 'order']



class QuizzesCreateForm(forms.ModelForm):
    """Form for creating a quiz."""
    class Meta:
        model = Quizzes
        fields = ['module', 'title', 'lesson', 'question', 'option1', 'option2', 'option3', 'answer']



        
class CourseEnrollmentForm(forms.ModelForm):
    """Form for enrolling in a course."""
    class Meta:
        model = CourseEnrollment
        fields = ['course', 'student', 'completed']