#List Form
from django.forms import ModelForm
from .models import *

#create user form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = '__all__'
        exclude = ['guest']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
