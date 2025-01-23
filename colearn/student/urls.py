from django.urls import path

from .views import *


urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('', student_profile, name='profile'),
    path('edit/', profile_edit_view, name='profile-edit'),
    path('onboarding/', profile_edit_view, name='profile-onboarding'),
    path('settings/', profile_settings_view, name='profile-settings'),
    path('emailchange/', profile_emailchange, name='email-change'),
    path('emailverify/', profile_emailverify, name='email-verify'),
    path('delete/', profile_delete_view, name='profile-delete'),

]