from django.urls import path
from .views import *


urlpatterns = [
    path('login/',login),
    path('add_phc/',add_phc),
    path('add_doctor/',add_doctor),

    path('',phome),
    path('details/<str:code>/',phc_details),

    
    path('<str:code>/',home),
    path('<str:code>/admission',admission),
    path('<str:code>/discharge',discharge),
    path('<str:code>/doctor_details',doctor_details)

]