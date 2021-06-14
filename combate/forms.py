from django import forms 
from django.forms import ModelForm
from .models import Parche 

class ParcheForm(ModelForm):
    class Meta:
        model = Parche
        fields = ['idParche','nombre', 'fechaParche', 'descParche']

