from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static
# Create your models here.

class User(AbstractUser):
    """Custom User model checks  the type of user"""
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    
class InstructorUser(models.Model):
    """Model for the instructor users in the platform."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # organization = models.CharField(m)

    def __str__(self):
        return self.user.username 

   

class StudentUser(models.Model):
    """Model for the student users in the platform."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    instructor = models.ForeignKey('InstructorUser', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class Profile(models.Model):
    """class for the user profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='avatars/', null=True, blank=True)
    display_name = models.CharField(max_length=100, null=True, blank=True)
    info = models.TextField(null=True, blank=True)


    def __str__(self):
        return str(self.user.username)
    
    @property
    def name(self):
        """Provide a username if the user doesn't provide one."""
        if self.display_name:
            name =  self.display_name
        else:
            name = self.user.username
        return name
    

    @property
    def avatar(self):
        """Provide a default avatar if the user doesn't provide one."""
        try:
            avatar = self.profile_pic.url

        except:
            avatar = static('images/avatar.png')
            
        return avatar
