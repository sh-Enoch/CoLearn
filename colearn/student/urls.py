from django.urls import path

from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentDetailView


urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

]