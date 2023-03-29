from django import forms
from .models import *

class PHCForm(forms.ModelForm):
    class Meta:
        model=PHC
        fields='__all__'

    
class DOCTORForm(forms.ModelForm):
    class Meta:
        model=medician
        fields='__all__'
