from django.urls import path
from .views import *


urlpatterns = [
    path('',login),
    path('add_phc/',add_phc),
    path('add_doctor/',add_doctor),
    
    path('<str:code>/',home),
    path('<str:code>/admission',Admission),
    path('<str:code>/discharge',discharge),
    path('<str:code>/doctor_details',doctor_details),
    path('<str:code>/admission_details',admission_details),
    path('<str:code>/discharge_details',discharge_details)

]