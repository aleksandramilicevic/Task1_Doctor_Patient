from django.urls import path, include
from . import views as v
from django.contrib import admin

urlpatterns = [
    path('', v.index,  name = 'index'),
    path('patient_register/', v.patient_register, name = 'patient_r'),
    path('doctor_register/', v.doctor_register, name = 'doctor_r'),
    path('registerpat/', v.registerpat, name = 'registerpat'),
    path('registerdoc/', v.registerdoc, name = 'registerdoc'),
    path('loginpat/', v.loginpat, name = 'loginpat'),
    path('logindoc/', v.logindoc, name = 'logindoc'),
    path('logoutpat/', v.logoutpat, name = 'logoutpat'),
    path('logoutdoc/', v.logoutdoc, name = 'logoutdoc'),
    path('patient_dashboard/', v.patient_dashboard, name = 'patient_dashboard'),
    path('doctor_dashboard/', v.doctor_dashboard, name = 'doctor_dashboard'),
    

]