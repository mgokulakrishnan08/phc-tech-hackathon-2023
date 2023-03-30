from django import forms
from .models import *


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = admission
        exclude = ['discharge_time','status', 'report','phc_id','discharge_status']

class DischargeForm(forms.ModelForm):
    class Meta:
        model = admission
        fields=['admission_no','discharge_status','report']

        
class PHCForm(forms.ModelForm):
    class Meta:
        model=PHC
        fields='__all__'

    
class DOCTORForm(forms.ModelForm):
    class Meta:
        model=medician
        fields='__all__'

class DesignationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DesignationForm,self).__init__(*args, **kwargs)
        self.fields['phc_id'] = forms.CharField(max_length=9)
        self.fields['medician_id'] = forms.CharField(max_length=9)


    class Meta:
        model=designation
        fields='__all__'
