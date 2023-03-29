from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

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

    return render(request, 'PHC/home.html',{'x':x})
   
def phome(request):
    return render(request, 'PHC/phome.html')

def phc_details(request):
    code ='PHC123456'
    obj= PHC.objects.get(phc_id=code)
    doctor=designation.objects.filter(phc_id=code)
    return render(request, 'PHC/phc_details.html',{'obj':obj,'doctor':doctor})