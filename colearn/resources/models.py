from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
class Resource(models.Model):
    """Resource model for storing course resources"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='resources/files/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)  # For external links
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
