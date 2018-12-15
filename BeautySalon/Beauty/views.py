from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from Beauty.models import Employee, Appointment

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html',{'form':form})
    
def logout(request):
    return HttpResponse("Chao chao")

def addEmployee(request, employee_id):
    e = Employee.objects.get(pk=employee_id)
    return HttpResponse("New Employee. %s" % e.name)

def appointments(request):
    list_appointments = Appointment.objects.all()
    context = {'list_appointments':list_appointments}
    return render(request, 'beauty/index.html', context)