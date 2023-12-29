from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

#using django libraries to create the form for login

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']