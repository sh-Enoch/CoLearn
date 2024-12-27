from django.db import models
from django.conf import settings
from users.models import CustomUser


# Create your models here.
user = CustomUser
class Course(models.Model):
    """create a  course model, core of the app."""
    title = models.CharField(max_length=15)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=12)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.title} - {self.course.title}"
    

class Enrollment(models.Model):
    """Allow for students to enroll to the course."""
    student = models.ForeignKey(user, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)