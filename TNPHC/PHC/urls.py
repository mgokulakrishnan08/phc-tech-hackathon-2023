from django.urls import path
from .views import *


urlpatterns = [
    path('',login),
    path('add_designation/',add_designation),
    path('phc_admin/',phc_admin),
    path('add_phc/',add_phc),
    path('add_doctor/',add_doctor),
    
    path('<str:code>/',home),
    path('<str:code>/admission',admission),
    path('<str:code>/discharge',discharge),
    path('<str:code>/doctor_details',doctor_details)

]