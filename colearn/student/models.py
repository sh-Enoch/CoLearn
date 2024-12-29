from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # is_student = models.BooleanField(default=False)
    # is_instructor = models.BooleanField(default=False)
    pass


class StudentUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    instructor = models.ForeignKey('InstructorUser', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class InstructorUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # organization = models.CharField(m)

    def __str__(self):
        return self.user.username 

   