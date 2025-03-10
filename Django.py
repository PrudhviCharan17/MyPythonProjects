# Basic auth app

Create a Login and Registration Page using MVC architecture in Django Framework
Creating a Login and Registration Page using the MVC architecture (Model-View-Controller) in Django involves creating models, views, and templates to handle user authentication and registration. Here's how you can do it step-by-step:
 
Step 1: Install Django and Start a Project
1.	Install Django:
pip install django
2.	Start a new Django project:
django-admin startproject user_auth_project
cd user_auth_project
3.	Create a new app for authentication:
python manage.py startapp auth_app
 
Step 2: Add the App to Installed Apps
Add the auth_app to the INSTALLED_APPS list in user_auth_project/settings.py:
INSTALLED_APPS = [
    ...
    'auth_app',
]
 
Step 3: Create a User Model
In auth_app/models.py, you can use Django's built-in User model for authentication. If needed, you can extend it:
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any custom fields here
    pass
 
Step 4: Define Forms
In auth_app/forms.py, create forms for registration and login:
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
 
Step 5: Create Views
In auth_app/views.py, define views for registration and login:
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'auth_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'auth_app/login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'auth_app/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
 
Step 6: Configure URLs
In auth_app/urls.py, define routes for the views:
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
Include the auth_app URLs in the project-level urls.py:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_app.urls')),
]
 
Step 7: Create Templates
1.	Registration Page (templates/auth_app/register.html):
<h2>Register</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
<a href="{% url 'login' %}">Login</a>
2.	Login Page (templates/auth_app/login.html):
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
<a href="{% url 'register' %}">Register</a>
3.	Dashboard Page (templates/auth_app/dashboard.html):
<h2>Welcome to your dashboard, {{ request.user.username }}!</h2>
<a href="{% url 'logout' %}">Logout</a>
 
Step 8: Apply Migrations and Run the Server
1.	Make migrations and migrate the database:
python manage.py makemigrations
python manage.py migrate
2.	Run the server:
python manage.py runserver
 
Step 9: Test the Application
1.	Visit http://127.0.0.1:8000/register/ to register a new user.
2.	Visit http://127.0.0.1:8000/login/ to log in.
3.	Upon login, you'll be redirected to the dashboard at http://127.0.0.1:8000/dashboard/.
4.	You can log out using the link on the dashboard.
 
This setup follows the MVC architecture:
•	Model: User model for data representation.
•	View: views.py for logic.
•	Controller: URLs mapping views to HTTP requests.
