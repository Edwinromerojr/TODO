#List Form
from django.forms import ModelForm
from .models import *


class ListForm(ModelForm):
    class Meta:
        model = List
        fields = '__all__'
