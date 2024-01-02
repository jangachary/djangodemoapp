# myapp/forms.py
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    
    class Meta:
        model = MyModel
        fields = ['name', 'email', 'role']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
