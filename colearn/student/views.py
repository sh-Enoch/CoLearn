from django.shortcuts import render, reverse, redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from  django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import StudentUser, InstructorUser
from .forms import StudentUserForm, ProfileForm, EmailForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from allauth.account.utils import send_email_confirmation
from django.contrib.auth import logout


class StudentListView(ListView):
    """View for the list of students"""
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    queryset = StudentUser.objects.all()


class StudentCreateView(CreateView):
    """View for creating a new student"""
    template_name = 'students/create_student.html'
    form_class = StudentUserForm

    def get_success_url(self):
        return reverse('student-list')
    

class StudentUpdateView(UpdateView):
    """View for updating a student"""
    template_name = 'students/update_student.html'
    form_class = StudentUserForm
    queryset = StudentUser.objects.all()

    def get_success_url(self):
        return reverse('student-list')

class StudentDeleteView(DeleteView):
    """View for deleting a student"""
    template_name = 'students/delete_student.html'
    queryset = StudentUser.objects.all()

    def get_success_url(self):
        return reverse('student-list')
    
class StudentDetailView(DetailView):
    """View for viewing a student"""
    template_name = 'students/student_detail.html'
    queryset = StudentUser.objects.all()
    context_object_name = 'student'


@login_required
def student_profile(request, username=None):
    """View for the student profile"""
    if username:
        profile = get_object_or_404(User, user__username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')
    return render(request, 'students/profile.html', {'student': profile})


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    if request.path == reverse('profile-onboarding'):
        onboarding = True

    else:
        onboarding = False
    
        

    return render(request, 'students/profile_edit.html', {'form': form, 'onboarding': onboarding})




@login_required
def profile_settings_view(request):
    return render(request, 'students/profile_settings.html')


@login_required
def profile_emailchange(request):

    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form':form})
    

    if  request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():

            #chack if email already exists.
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f'{email} is already in use.')
                return redirect('profile-settings')

            form.save()

            #signal to update. and set verified to false.
            send_email_confirmation(request, request.user)
            return redirect('profile-settings')
        else:
            messages.warning(request, "Form not valid")
            return redirect('profile-settings')

    return redirect('home')


@login_required
def profile_emailverify(request):
    """Verify user email"""
    send_email_confirmation(request, request.user)
    return redirect('profile-settings')


@login_required
def profile_delete_view(request):
    """Delete a users profile."""
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, "Account deleted.")
        return redirect('home')

    return render(request, 'students/profile_delete.html')