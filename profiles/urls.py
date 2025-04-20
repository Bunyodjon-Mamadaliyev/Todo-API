from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    UserDetailView,
    PasswordResetRequestView,
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/logout/', LogoutView.as_view(), name='auth-logout'),
    path('auth/user/', UserDetailView.as_view(), name='current_user'),
    path('auth/password/reset/', PasswordResetRequestView.as_view(), name='password_reset'),
]

