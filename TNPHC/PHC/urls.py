from django.urls import path
from .views import *


urlpatterns = [
    path('add_designation/',add_designation),
    path('phc_admin/',phc_admin),
    path('add_phc/',add_phc),
    path('add_doctor/',add_doctor),

    path('',phome),
    path('details/<str:code>/',phc_details),

    path('login/',login),
    path('<str:code>/',home),
    path('<str:code>/admission',Admission),
    path('<str:code>/discharge',discharge),
    path('<str:code>/doctor_details',doctor_details)

]