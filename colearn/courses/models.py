from django.db import models
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field
from resources.models import Tag


class Course(models.Model):
    """Model for the courses in the platform."""
    title = models.CharField(max_length=120)
    description = models.TextField()
    summary = models.TextField(default='This is cool!')
    featured = models.BooleanField(default=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('student.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} - {self.summary}"

    def clean(self):
        """Custom validation for the Course model."""
        if len(self.title) < 5:
            raise ValidationError("Course title must be at least 5 characters long.")
        if len(self.description) < 20:
            raise ValidationError("Course description must be at least 20 characters long.")
        if not self.creator:
            raise ValidationError("A course must have a creator assigned.")


class Modules(models.Model):
    """Model for the modules in the course."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.course.title}"

    def clean(self):
        """Custom validation for the Modules model."""
        if self.order < 0:
            raise ValidationError("Module order cannot be negative.")
        if len(self.title) < 5:
            raise ValidationError("Module title must be at least 5 characters long.")
        if not self.course:
            raise ValidationError("A module must be associated with a course.")


class Lessons(models.Model):
    """Model for the lessons in the course."""
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = CKEditor5Field('Content', config_name='extends')
    video_url = models.URLField(null=True, blank=True, max_length=200)
    duration = models.DurationField(null=True, blank=True, help_text='Duration of the video eg 00:10:00 for 10 minutes')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.module} > {self.module.title} > {self.title}"

    def clean(self):
        """Custom validation for the Lessons model."""
        if len(self.title) < 5:
            raise ValidationError("Lesson title must be at least 5 characters long.")
        if not self.content:
            raise ValidationError("Lesson content cannot be empty.")
        if self.order < 0:
            raise ValidationError("Lesson order cannot be negative.")
        if self.duration and self.duration.total_seconds() <= 0:
            raise ValidationError("Duration must be a positive value.")


class Quizzes(models.Model):
    """Model for the quizzes in the course."""
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default='Knowledge Check')
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)

    options = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]

    answer = models.CharField(max_length=200, choices=options)

    def __str__(self):
        return f"{self.lesson}: {self.title}"

    def clean(self):
        """Custom validation for the Quizzes model."""
        if self.answer not in ['option1', 'option2', 'option3']:
            raise ValidationError("Answer must match one of the options (option1, option2, option3).")
        if not self.question.strip():
            raise ValidationError("Question cannot be empty.")
        if not all([self.option1, self.option2, self.option3]):
            raise ValidationError("All options (option1, option2, and option3) must be filled in.")


class CourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey('student.User', on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    @property
    def progress(self):
        """Calculate and return the student's progress in the course."""
        total_lessons = self.course.modules.all().aggregate(
            total_lessons=models.Count('lessons')
        )['total_lessons'] or 0

        completed_lessons = self.course.modules.filter(
            lessons__completed_by=self.student
        ).count()

        if total_lessons > 0:
            return f"{(completed_lessons / total_lessons) * 100:.2f}%"
        return "0%"

    def __str__(self):
        return f"{self.course.title} - {self.student.username}"
        
class Resource(models.Model):
    """Model for resources related to lessons."""
    RESOURCE_TYPES = [
        ('PDF', 'PDF Document'),
        ('LINK', 'Web Link'),
        ('VIDEO', 'Video File'),
        ('IMAGE', 'Image File'),
        ('OTHER', 'Other File Type'),
    ]

    lesson = models.ForeignKey('Lessons', on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES, default='OTHER')
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.lesson.title}: {self.title}"

    def clean(self):
        """Custom validation for the Resource model."""
        if not self.file and not self.link:
            raise ValidationError("A resource must have either a file or a link.")
        if self.file and self.link:
            raise ValidationError("A resource cannot have both a file and a link.")
        if self.resource_type == 'LINK' and not self.link:
            raise ValidationError("For a 'Web Link' resource, a valid URL must be provided.")
        if self.resource_type != 'LINK' and not self.file:
            raise ValidationError(f"For a {self.resource_type} resource, a file must be provided.")

