__author__ = 'foste4jd'
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from express.models import UserLogin, Client, Product, Aed, Battery, Eyewash, Service
from django.contrib.auth.models import User
from django.forms.widgets import Input
from datetime import date

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ('user_type','first_name','last_name')

# class ServiceForm(forms.ModelForm):
#     class Meta:
#         model = Service
# #        fields = ('service_type', 'service_id', 'client', 'product', 'service_date', 'next_service_date')
#         widgets = {
#                 #'service_type': CharField(attrs={}),
#             }

# class InstallForm(forms.ModelForm):
#     class Meta:
#         model = Service

class LocationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('location',)


class ServiceInstallForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('user_login', 'client')

class ProductInstallForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('client', 'location', 'product_type', 'product_id', 'expiration_date')
