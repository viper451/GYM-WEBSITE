from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(forms.ModelForm):

	class Meta:
		model=Registeration
		fields=['firstname','lastname','age','gender','phonenumber','offer','modeofpayment']




class FitnessForm(forms.ModelForm):

	class Meta:
		model=Fit
		fields=['age','flexibility','fitness','aerobic','gender']

     

class CreateUserForm(UserCreationForm):
    class Meta:
	    model = User 
	    fields = ['username', 'email','password1','password2']



   
