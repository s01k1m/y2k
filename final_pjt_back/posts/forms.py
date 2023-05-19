from django import forms
from .models import Stills

class StillsForm(forms.ModelForm):
    
    class Meta:
        model = Stills
        fields = ("",)
