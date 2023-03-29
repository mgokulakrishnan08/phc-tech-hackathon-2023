from django.urls import path
from .views import *


urlpatterns = [
    path('',phome),
    path('phc_details/',phc_details),
    path('login/',login),
    path('<str:code>/',home),

]