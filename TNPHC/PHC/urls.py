from django.urls import path
from .views import *


urlpatterns = [
    path('phc_admin/',phc_admin),
    path('<int:choice>/analyze',analyze),
    path('add_designation/',add_designation),
    path('add_phc/',add_phc),
    path('add_doctor/',add_doctor),

    path('',phome),
    path('details/<str:code>/',phc_details),

    path('login/',login),
    path('<str:code>/home',home),
    path('<str:code>/admission',Admission),
    path('<str:code>/discharge',discharge),
    path('<str:code>/doctor_details',doctor_details),
    path('<str:code>/admission_details',admission_details),
    path('<str:code>/discharge_details',discharge_details)

]