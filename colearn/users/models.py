from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
"""Create a student_user model and instructor_user model"""

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    expertise = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    interests = models.CharField(max_length=100, blank=True, null=True)
    enrolled_courses = models.PositiveIntegerField(default=0)

    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',  # Avoiding conflict with the default User model
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_set',  # Avoiding conflict with the default User model
        blank=True
    )

