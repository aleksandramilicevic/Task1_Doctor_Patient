from click import password_option
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render 
from django.contrib.auth import authenticate, login
# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'groupbtn.html')


def patient_register(request):
    if request.method == "POST":

      username= request.POST.get('username')  
      name = request.POST.get('name') 
      surname = request.POST.get('surname') 
      email = request.POST.get('email') 
      address= request.POST.get('address') 
      password = request.POST.get('password') 
      confirm_password = request.POST.get('confirm a password') 

      myuser = User.objects.create_user(username, email, password)
      myuser.first_name = name
      myuser.last_name = surname
      myuser.address = address
      myuser.confirm_password = confirm_password
      myuser.save()
      messages.succes(request, "Your account has been successfully created!" )
     

    return render(request, 'patient_register.html')

def doctor_register(request):
    if request.method == "POST":

      username= request.POST.get('username')  
      name = request.POST.get('name') 
      surname = request.POST.get('surname') 
      email = request.POST.get('email') 
      address= request.POST.get('address') 
      password = request.POST.get('password') 
      confirm_password = request.POST.get('confirm a password') 

      docuser = User.objects.create_user(username, email, password)
      docuser.first_name = name
      docuser.last_name = surname
      docuser.address = address
      docuser.confirm_password = confirm_password
      docuser.save()
      messages.succes(request, "Your account has been successfully created!" )
     
    return render(request, 'doctor_register.html')

def registerpat(request):
    return render(request, 'registerpat.html')

def registerdoc(request):
    return render(request, 'registerdoc.html')

def loginpat(request):
    if request.method == "POST":

      username= request.POST.get('username') 
      password = request.POST.get('password') 

      user = authenticate(username = username, password = password)
      if user is not None:
          login(request, user)
      else:
          messages.error(request, "Username or password is incorrect!")
    return render(request, 'loginpat.html')

def logindoc(request):
    if request.method == "POST":

      username= request.POST.get('username') 
      password = request.POST.get('password') 

      user = authenticate(username = username, password = password)
      if user is not None:
          login(request, user)
      else:
          messages.error(request, "Username or password is incorrect!")
    return render(request, 'logindoc.html')

def logoutpat(request):
    pass

def logoutdoc(request):
    pass
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
