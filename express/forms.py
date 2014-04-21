__author__ = 'foste4jd'
from django import forms
from express.models import UserLogin, Client, Product, Aed, Battery, Eyewash, Service
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.widgets import Input

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

        def __init__(self, username=None, *args, **kwargs):
                super(ServiceForm, self).__init__(*args, **kwargs)

                try:
                        if not username == None:
                                self.fields['user'].queryset = Use.objects.filter(pk=username.user.id)
                except:
                        raise ValueError("No username supplied. %s" & e)

                self.fields['service_type'].widget = forms.HiddenInput()
                self.fields['client'].widget = forms.HiddenInput()
                #self.fields['location'].widget = forms.HiddenInput()
                self.fields['product'].widget = forms.HiddenInput()
                #self.fields['product_type'].widget = forms.HiddenInput()


        class Meta:
                model = Service
                #widgets = dict(amt=Html5NumberInput({'required': True,'max':999,'min':0,'step':.01}))


    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data["first_name"]
    #     user.last_name = self.cleaned_data["last_name"]
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user
