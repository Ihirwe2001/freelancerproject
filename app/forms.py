from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Contact

class UserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "w-full p-2 border rounded-md"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "w-full p-2 border rounded-md"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "w-full p-2 border rounded-md"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password", "class": "w-full p-2 border rounded-md"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']