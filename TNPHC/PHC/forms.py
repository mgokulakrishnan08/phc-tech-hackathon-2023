from django import forms
from .models import *


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = admission
        exclude = ['discharge_time','status', 'report','phc_id','discharge_status']




class DischargeForm(forms.ModelForm):
     class Meta:
         model = admission
         fields=['admission_no','discharge_status']


# class DischargeForm(forms.Form):
#     admission_no=forms.CharField(max_length=10)
#     discharge_status=forms.CharField(max_length=500)
#     #report=forms.FileField()


    

        
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

    def clean(self):
        self.cleaned_data['phc_id']=PHC(phc_id=self.cleaned_data['phc_id'])
        self.cleaned_data['medician_id']=medician(medician_id=self.cleaned_data['medician_id'])
        return super(DesignationForm, self).clean()




