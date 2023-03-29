from django import forms
from .models import *


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = admission
        exclude = ['discharge_time','status', 'report','phc_id']

class DischargeForm(forms.ModelForm):
    class Meta:
        model = admission
        fields=['admission_no','discharge_status','report']