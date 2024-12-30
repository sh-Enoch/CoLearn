from django.db import models

# Create your models here.

class Course(models.Model):
    """Model for the courses in the platform"""
    title = models.CharField(max_length=120)
    description = models.TextField()
    summary = models.TextField(default='This is cool!')
    featured = models.BooleanField(default=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('student.User', on_delete=models.CASCADE, null=True)   

    def __str__(self):
        """Return the title of the course and the summary"""
        return f"{self.title} - {self.summary}"
    


class Modules(models.Model):
    """Model for the modules in the course"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        """Return the title of the module and the course it belongs to"""
        return f"{self.title} - {self.course.title}"



class Lessons(models.Model):
    """Model for the lessons in the course"""
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    video_url = models.URLField(null=True, blank=True,max_length=200)
    duration = models.DurationField(null=True, blank=True, help_text='Duration of the video eg 00:10:00 for 10 minutes')
    order = models.PositiveIntegerField(default=0)
    # resources = models.ManyToManyField('resources.Resource', blank=True)

    class Meta:
        ordering = ['order']


    def __str__(self):
        """Return the title of the lesson and the module it belongs to"""
        return f"{self.title} - {self.module.title}"


