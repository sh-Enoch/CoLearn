from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, ModuleListView, LessonListView, ModuleDetailView
from .views import ModuleUpdateView, LessonUpdateView, ModuleDeleteView, LessonDeleteView, LessonDetailView, ModuleCreateView, LessonCreateView
from .views import  CourseEnrollmentListView, CourseEnrollmentDetailView, CourseEnrollmentUpdateView, CourseEnrollmentDeleteView, CourseEnrollmentView
from .views import QuizzesListView, QuizzesDetailView, QuizzesUpdateView, QuizzesCreateView, QuizzesDeleteView
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

    # "enrollment" paths
    path('enrollment/', CourseEnrollmentListView.as_view(), name='course-enrollment-list'),
    path('enroll/', CourseEnrollmentView.as_view(), name='course-enroll'),
    path('enroll/<int:pk>/', CourseEnrollmentView.as_view(), name='course-enroll'),
    path('enrollment/<int:pk>/delete/', CourseEnrollmentDeleteView.as_view(), name='course-enrollment-delete'),
    path('enrollment/<int:pk>/update/', CourseEnrollmentUpdateView.as_view(), name='course-enrollment-update'),
    path('enrollment/<int:pk>/', CourseEnrollmentDetailView.as_view(), name='course-enrollment-detail'),

    #path to handle quizses list, detail, update, create and delete
    path('quizzes/<int:pk>/delete/', QuizzesDeleteView.as_view(), name='quizzes-delete'),
    path('quizzes/<int:pk>/update/', QuizzesUpdateView.as_view(), name='quizzes-update'),
    path('quizzes/<int:pk>/', QuizzesDetailView.as_view(), name='quizzes-detail'),
    path('quizzes/', QuizzesListView.as_view(), name='quizzes-list'),
    path('quizzes/create/', QuizzesCreateView.as_view(), name='quizzes-create'),

]