__author__ = 'prabhath'

from django import forms
from .models import SignUp, CreateLogin


# create form that can be used
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["first_name", "last_name", "email"]


# class Name(forms.ModelForm):
#     class Meta:
#         model = UserNames
#         fields = ["name"]


class CreateLoginForm(forms.ModelForm):
    class Meta:
        model = CreateLogin
        model.password = forms.CharField(widget=forms.HiddenInput())
        #widgets = {'password': forms.HiddenInput()}
        fields = ["first_name", "last_name", "email", "password"]
