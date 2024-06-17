from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
