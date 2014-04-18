__author__ = 'foste4jd'
from django import forms
from express.models import UserLogin, Client, Product, Aed, Battery, Eyewash, Service
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.widgets import Input

class userloginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")

class userprofileform(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ('user_type','first_name','last_name')




    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data["first_name"]
    #     user.last_name = self.cleaned_data["last_name"]
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user
