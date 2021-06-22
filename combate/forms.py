from django import forms 
from django.forms import ModelForm, widgets
from .models import Parche 

class ParcheForm(ModelForm):
    class Meta:
        model = Parche
        fields = ['idParche','nombre', 'fechaParche', 'descParche']

        widgets ={
            'fechaParche' : forms.DateInput(format=('%Y/%m/%d'), attrs={'type':'date'})
        }
  

