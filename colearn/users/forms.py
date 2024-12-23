from django.forms import ModelForm
from .models import CustomUser as User
from django import forms

class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_pic', 'interests']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password'}),
            'bio': forms.Textarea(attrs={'placeholder':'Bio'}),
            'interests': forms.TextInput(attrs={'placeholder':'Interests'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'profile_pic': forms.FileInput(attrs={'placeholder':'Profile Picture'}) 
        }
     


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password'})
        }