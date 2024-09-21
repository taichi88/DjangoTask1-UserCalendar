from django import forms
from .models import Person
from django.db import models


class PersonForm(forms.ModelForm):



    class Meta:
        model = Person
        fields = ['name','birthdate', 'number',
                  ]
        widgets = {
            "name": forms.TextInput(attrs={'type': 9}),
            "birthdate": forms.DateInput(attrs={'type': 'date'}),
            
           
        }
        help_texts = {
            'name': 'Enter name used in ID',
            
            'birthdate': 'Enter mm/dd/yyyy',
            'number': 'Enter number',
            
        }


