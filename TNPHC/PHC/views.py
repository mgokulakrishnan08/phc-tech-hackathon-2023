from django.shortcuts import render,redirect
from django.db.models import Subquery
from django.http import HttpResponse
from .models import *
from .forms import *
from datetime import datetime,date  
import random  as r


# Create your views here.
# public views
def phome(request):
    obj=''
    if request.GET:
        pincode =request.GET.dict()['pincode']
        obj = PHC.objects.filter(pincode=pincode)

    return render(request, 'PHC/phome.html',{'obj':obj})



def phc_details(request, code):
    obj= PHC.objects.get(phc_id=code)
    doctor=designation.objects.filter(phc_id=code)
    return render(request, 'PHC/phc_details.html',{'obj':obj,'doctor':doctor})



# admin views
def phc_admin(request):
    if request.GET:
        choice=request.GET.dict()['choice']
        return redirect(f'/{choice}/analyze')
    no_of_phc=PHC.objects.all().count()
    no_of_active_inpatients=admission.objects.filter(discharge_time__isnull=True).count()
    no_of_admissions=admission.objects.all().count()
    no_of_doctors=medician.objects.all().count()
    dict={'no_of_phc':no_of_phc,
           'no_of_active_inpatients':no_of_active_inpatients,
             'no_of_admissions':no_of_admissions,
             'no_of_doctors':no_of_doctors}         
    return render(request, 'PHC/phc_admin.html', dict)



def analyze(request, choice):
    x=''
    if choice==1:
        if request.GET:
            from_date = request.GET.dict()['from'] 
            to = request.GET.dict()['to']
            print(from_date)
            #in particular yr
            x = admission.objects.filter(admission_time__gte=from_date, admission_time__lte=to)
    elif choice==2:
        if request.GET:
            pincode = request.GET.dict()['pincode'] 
            from_date = request.GET.dict()['from'] 
            to = request.GET.dict()['to']
            print(from_date)
            #in particular yr
            xx = PHC.objects.filter(pincode=pincode)
            x = admission.objects.filter(phc_id__in=Subquery(xx.values('phc_id')), admission_time__gte=from_date, admission_time__lte=to)
    elif choice==3:
        if request.GET:
            phc_id = request.GET.dict()['phc_id'] 
            from_date = request.GET.dict()['from'] 
            to = request.GET.dict()['to']
            print(from_date)
            #in particular yr
            x = admission.objects.filter(phc_id=phc_id, admission_time__gte=from_date, admission_time__lte=to)

 


    return render(request, 'PHC/analyze.html',{'choice':choice,'x':x})


def add_phc(request):
    if request.method == 'POST':
            form = PHCForm(request.POST, request.FILES)
            if form.is_valid():
                obj=form.save(commit=False)
                phc_id='PHC' + str(r.randint(1000000,9999999))
                obj.phc_id=phc_id
                phc_name=form.cleaned_data['phc_name']
                obj.save()
                return HttpResponse(f'<center>PHC added<br>PHC ID:{phc_id}<br>PHC NAME:{phc_name}</center>')

    else:
        form = PHCForm()
                    
    return render(request, 'PHC/add_phc.html',{'form':form})

def add_doctor(request):
    if request.method == 'POST':
            form = DOCTORForm(request.POST, request.FILES)
            if form.is_valid():
                obj=form.save(commit=False)
                medician_id='DOC' + str(r.randint(1000000,9999999))
                obj.medician_id=medician_id
                medician_name=form.cleaned_data['name']
                obj.save()
                return HttpResponse(f'<center>Doctor Added<br>MEDICIAN ID:{medician_id}<br>MEDICIAN NAME:{medician_name}</center>')
    else:
        form = DOCTORForm()
                   
    return render(request, 'PHC/add_doctor.html',{'form':form})



def add_designation(request):
    if request.method == 'POST':
            form = DesignationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse('<center>Designation  added</center>')
    else:
        form = DesignationForm()
    return render(request, 'PHC/add_designation.html',{'form':form})




# PHC views
def login(request):
    if request.GET:
        phc_id=request.GET.dict()['phc_id']
        password=request.GET.dict()['password']
        if password==PHC.objects.get(phc_id=phc_id).password:
            return redirect(f'/{phc_id}/home')       
    return render(request, 'PHC/login.html')



def home(request,code):
    x=PHC.objects.get(phc_id=code)
    doc=designation.objects.get(phc_id=code,role="Dean")
    no_of_patients=admission.objects.filter(phc_id=code,discharge_time__isnull=True).count()
    return render(request, 'PHC/home.html',{'x':x,'code':code,'doc':doc,'no_of_patients':no_of_patients})
   
   

   

def Admission(request,code):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            admission_no=code[3:] + str(date.today()).replace('-','') + str(r.randint(100,999))
            obj.admission_no=admission_no
            obj.phc_id=PHC(phc_id=code)
            obj.save()
            return HttpResponse(f'<center>Admission entered<br>Admission no.:{admission_no}</center>')
    else:
        form = AdmissionForm()
    return render(request, 'PHC/admission.html',{'form':form,'code':code})


   
def discharge(request,code):
    if request.method == 'POST':
        form = DischargeForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data['admission_no'])
            obj=admission.objects.get(admission_no=form.cleaned_data['admission_no'])
            obj.discharge_status=form.cleaned_data['discharge_status']
            #obj.report=form.cleaned_data['report']
            obj.discharge_time=datetime.now()
            obj.save()

            return HttpResponse('<center>added</center>')
    else:
        form = DischargeForm()
    return render(request, 'PHC/discharge.html',{'form':form,'code':code})



   
def doctor_details(request,code):
    doctor=designation.objects.filter(phc_id=code)
    return render(request, 'PHC/doctor_details.html',{'doctor':doctor,'code':code})



def admission_details(request,code):
    obj=admission.objects.filter(phc_id=code, discharge_time__isnull=True)
    return render(request, 'PHC/admission_details.html',{'obj':obj,'code':code})



def discharge_details(request,code):
    obj=admission.objects.filter(phc_id=code, discharge_time__isnull=False)
    return render(request, 'PHC/discharge_details.html',{'obj':obj,'code':code})


