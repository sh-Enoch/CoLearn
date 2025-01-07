from django.urls import path
from .views import HomePageView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView, 
    PasswordResetDoneView
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
]