__author__ = 'prabhath'

from django import forms
from .models import SignUp


# create form that can be used
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["first_name", "last_name", "email"]


# class Name(forms.ModelForm):
#     class Meta:
#         model = UserNames
#         fields = ["name"]
