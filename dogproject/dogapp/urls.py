# dogapp/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('random_dog/', views.random_dog, name='random_dog'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='dogapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
