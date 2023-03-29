from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from datetime import datetime    


# Create your views here.
def login(request):
    if request.GET:
        phc_id=request.GET.dict()['phc_id']
        password=request.GET.dict()['password']
        if password==PHC.objects.get(phc_id=phc_id).password:
            return redirect(f'{phc_id}/') 
            

    return render(request, 'PHC/login.html')



def home(request,code):
    x=PHC.objects.get(phc_id=code)

    return render(request, 'PHC/home.html',{'x':x, 'code':code})
   

def admission(request,code):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.phc_id=PHC(phc_id=code)
            obj.save()
            return HttpResponse('<center>added</center>')
    else:
        form = AdmissionForm()
    return render(request, 'PHC/admission.html',{'form':form})
   
def discharge(request,code):
    if request.method == 'POST':
        form = DischargeForm(request.POST, request.FILES)
        if form.is_valid():
            obj=admission.objects.get(admission_no=form.cleaned_data['admission_no'])
            obj.discharge_status=form.cleaned_data['discharge_status']
            obj.report=form.cleaned_data['report']
            obj.discharge_time=datetime.now()
            obj.save()

            return HttpResponse('<center>added</center>')
    else:
        form = DischargeForm()
    return render(request, 'PHC/discharge.html',{'form':form})
   