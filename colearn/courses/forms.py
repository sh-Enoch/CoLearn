from .models import Course, Modules, Lessons, Quizzes, CourseEnrollment, Resource
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

class CourseCreateForm(forms.ModelForm):
    """Form for creating a course."""
    class Meta:
        model = Course
        fields = ['title', 'description', 'summary', 'featured', 'creator']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a detailed description'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief summary'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'creator': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Course Title',
            'description': 'Course Description',
            'summary': 'Course Summary',
            'featured': 'Is Featured?',
            'creator': 'Course Creator',
        }


class ModulesCreateForm(forms.ModelForm):
    """Form for creating a module."""
    class Meta:
        model = Modules
        fields = ['course', 'title', 'description', 'order']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter module title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter module description'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter module order'}),
        }
        labels = {
            'course': 'Select Course',
            'title': 'Module Title',
            'description': 'Module Description',
            'order': 'Order in Course',
        }


class LessonsCreateForm(forms.ModelForm):
    """Form for creating a lesson."""
    content = forms.CharField(widget=CKEditor5Widget(config_name='extends'))
    
    class Meta:
        model = Lessons
        fields = ['module', 'title', 'content', 'video_url', 'duration', 'order']
        widgets = {
            'module': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lesson title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter lesson content'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter video URL'}),
            'duration': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM:SS'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter lesson order'}),
        }
        labels = {
            'module': 'Select Module',
            'title': 'Lesson Title',
            'content': 'Lesson Content',
            'video_url': 'Video URL (Optional)',
            'duration': 'Video Duration (Optional)',
            'order': 'Order in Module',
        }


class QuizzesCreateForm(forms.ModelForm):
    """Form for creating a quiz."""
    class Meta:
        model = Quizzes
        fields = ['module', 'title', 'lesson', 'question', 'option1', 'option2', 'option3', 'answer']
        widgets = {
            'module': forms.Select(attrs={'class': 'form-control'}),
            'lesson': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter quiz title'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter quiz question'}),
            'option1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option 1'}),
            'option2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option 2'}),
            'option3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option 3'}),
            'answer': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'module': 'Select Module',
            'lesson': 'Select Lesson',
            'title': 'Quiz Title',
            'question': 'Quiz Question',
            'option1': 'Option 1',
            'option2': 'Option 2',
            'option3': 'Option 3',
            'answer': 'Correct Answer',
        }

    def clean_answer(self):
        """Ensure the selected answer is one of the options."""
        answer = self.cleaned_data.get('answer')
        options = [self.cleaned_data.get('option1'), self.cleaned_data.get('option2'), self.cleaned_data.get('option3')]
        if answer not in ['option1', 'option2', 'option3']:
            raise forms.ValidationError("The answer must be one of the provided options.")
        return answer


class CourseEnrollmentForm(forms.ModelForm):
    """Form for enrolling in a course."""
    class Meta:
        model = CourseEnrollment
        fields = ['course', 'student', 'completed']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'course': 'Select Course',
            'student': 'Select Student',
            'completed': 'Completed?',
        }


class ResourceCreateForm(forms.ModelForm):
    """Form for creating a resource."""
    class Meta:
        model = Resource
        fields = ['lesson', 'title', 'description', 'resource_type', 'file', 'link']

    def clean(self):
        """Custom validation for the Resource form."""
        cleaned_data = super().clean()
        resource_type = cleaned_data.get('resource_type')
        file = cleaned_data.get('file')
        link = cleaned_data.get('link')

        if not file and not link:
            raise forms.ValidationError("A resource must have either a file or a link.")
        if file and link:
            raise forms.ValidationError("A resource cannot have both a file and a link.")
        if resource_type == 'LINK' and not link:
            raise forms.ValidationError("For a 'Web Link' resource, a valid URL must be provided.")
        if resource_type != 'LINK' and not file:
            raise forms.ValidationError(f"For a {resource_type} resource, a file must be provided.")

        return cleaned_data