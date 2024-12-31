from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, ModuleListView, LessonListView, ModuleDetailView
from .views import ModuleUpdateView, LessonUpdateView, ModuleDeleteView, LessonDeleteView, LessonDetailView, ModuleCreateView, LessonCreateView
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),

    #path to view module and lesson list
    path('module/', ModuleListView.as_view(), name='module-list'),
    path('lesson/', LessonListView.as_view(), name='lesson-list'),

    #detail views for modules and lessons
    path('module/<int:pk>', ModuleDetailView.as_view(), name='module-detail'),
    path('lesson/<int:pk>', LessonDetailView.as_view(), name='lesson-detail'),

    #create lesson and module paths
    path('module/create/', ModuleCreateView.as_view(), name='module-create'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson-create'),


    #path to update and delete modules and lessons
    path('module/<int:pk>/update/', ModuleUpdateView.as_view(), name='module-update'),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson-update'),

    #path to delete modules and lessons 
    path('module/<int:pk>/delete/', ModuleDeleteView.as_view(), name='module-delete'),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson-delete'),

]