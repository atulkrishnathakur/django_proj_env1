from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from myadmin.models.country import Country

class CountryForm(ModelForm):
  class Meta:
    model = Country
    fields = ['country_name']
    labels = {'country_name':'Country Name*'}
    widgets = {
         'country_name':forms.TextInput(attrs={'class':"form-control",'style':'max-width:300px;', 'placeholder':'Country Name',}),
             }
    
