from .models import Register, Profile
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.core.validators import *
class RegisterForm(ModelForm):
    class Meta:
        model=Register
        fields = ['Fullname', 'Email', 'Phone', 'Username', 'Password', 'Confirm_password']

        widgets = {
            'Fullname': forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'Phone': forms.NumberInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'Username': forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'Confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


#for registration of owner:
class UserForm(UserCreationForm):
    fullname = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    phone = forms.CharField()

    class Meta:
        model = User
        fields = ('fullname', 'email', 'phone', 'username', 'password1', 'password2')


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user','username']