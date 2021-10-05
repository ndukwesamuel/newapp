from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from leads.models import *


User = get_user_model()


class Createform(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields =   {"username"}
        field_classes = {'username':UsernameField}
