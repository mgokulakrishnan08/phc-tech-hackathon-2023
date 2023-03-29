from django.urls import path
from .views import *


urlpatterns = [
    path('',login),
    path('add_phc/',add_phc),
    path('add_doctor/',add_doctor),
    path('<str:code>/',home),
    path('<str:code>/doctor_details',doctor_details)

]