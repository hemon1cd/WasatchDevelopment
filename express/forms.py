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

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('service_type', 'service_id', 'client', 'product', 'service_date', 'next_service_date')
        widgets = {
                #'service_type': CharField(attrs={}),
            }


#        def __init__(self, client=None, *args, **kwargs):
#            super(ServiceForm, self).__init__(*args, **kwargs)
#
#            try:
#                if not client == None:
#                    self.fields['user_login'].queryset = Client.objects.filter(pk=client.product.id)
#            except:
#                raise ValueError("No username supplied. %s" & e)

           #self.fields['service_type'].widget = forms.HiddenInput()
           #self.fields['client'].widget = forms.HiddenInput()
           #self.fields['location'].widget = forms.HiddenInput()
           #self.fields['product'].widget = forms.HiddenInput()
           #self.fields['product_type'].widget = forms.HiddenInput()

    
           #widgets = dict(amt=Html5NumberInput({'required': True,'max':999,'min':0,'step':.01}))


    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data["first_name"]
    #     user.last_name = self.cleaned_data["last_name"]
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user

