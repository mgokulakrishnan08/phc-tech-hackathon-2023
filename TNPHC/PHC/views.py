from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
# admin views
def add_phc(request):
    if request.method == 'POST':
            form = PHCForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse('<center>PHC added</center>')

    else:
        form = PHCForm()
                    
    return render(request, 'PHC/add_phc.html',{'form':form})

def add_doctor(request):
    if request.method == 'POST':
            form = DOCTORForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse('<center>Doctor Added</center>')
    else:
        form = DOCTORForm()
                    
    return render(request, 'PHC/add_doctor.html',{'form':form})




# PHC views
def login(request):
    if request.GET:
        phc_id=request.GET.dict()['phc_id']
        password=request.GET.dict()['password']
        if password==PHC.objects.get(phc_id=phc_id).password:
            return redirect(f'{phc_id}/') 
            

    return render(request, 'PHC/login.html')



def home(request,code):
    x=PHC.objects.get(phc_id=code)
    return render(request, 'PHC/home.html',{'x':x,'code':code})
   

def doctor_details(request,code):
    doctor=designation.objects.filter(phc_id=code)
    return render(request, 'PHC/doctor_details.html',{'doctor':doctor})
