from django.urls import path
from .views import HomePageView
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]