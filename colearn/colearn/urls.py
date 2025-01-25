"""
URL configuration for colearn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
from student.views import student_profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('student/', include('student.urls')),
    path('courses/', include('courses.urls')),
    path('profile/', include('student.urls')),
    path('accounts/', include('allauth.urls')),
    path('resources/', include('resources.urls')),
    path('@<username>/', student_profile, name='profile'),
]
urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
