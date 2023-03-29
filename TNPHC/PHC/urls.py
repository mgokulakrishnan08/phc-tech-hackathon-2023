from django.urls import path
from .views import *


urlpatterns = [
    path('',login),
    path('<str:code>/',home),
    path('<str:code>/doctor_details',doctor_details)

]