from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Confirm Password"}))
    #email = forms.EmailField(required=True)

    class meta:
        model=User
        fields= ['username','email']