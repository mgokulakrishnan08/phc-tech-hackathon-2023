from django.urls import path
from .views import *


urlpatterns = [
    path('',login),
    path('<str:code>/',home),
    path('<str:code>/admission',admission),
    path('<str:code>/discharge',discharge),
]