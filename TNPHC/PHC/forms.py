from django import forms
from .models import *


class AdmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdmissionForm,self).__init__(*args, **kwargs)
        TYPE_SELECT=(('Male','Male'),('Female','Female'),('Others','Others'))
        self.fields['gender'] = forms.ChoiceField(choices=TYPE_SELECT,widget=forms.RadioSelect())
      

    class Meta:
        model=admission
        exclude=['phc_id']

        




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
    def __init__(self, *args, **kwargs):
        super(DOCTORForm,self).__init__(*args, **kwargs)
        TYPE_SELECT=(('Male','Male'),('Female','Female'),'Others','Others')
        self.fields['gender'] = forms.ChoiceField(choices=TYPE_SELECT,widget=forms.RadioSelect())
      

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




