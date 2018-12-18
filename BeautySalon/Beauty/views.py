from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    RetrieveAPIView, 
    RetrieveUpdateAPIView, 
    )

from Beauty.forms import EmployeeForm
from Beauty.models import Employee, Appointment
from Beauty.serializers import (
    AppointmentSerializer,
    AppointmentCreateSerializer,
    EmployeeSerializer,
    EmployeeCreateSerializer,    
    )

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
    
def addEmployee(request, employee_name):
    e = Employee(name = employee_name)
    e.save()
    return HttpResponse(request,"beauty/employees.html", None)

def employees(request):
    return render(request, 'beauty/employees.html',None)

def addAppointment(request):
    return render(request, 'beauty/appointments/addappointment.html',None)
def updateAppointment(request):
    return render(request, 'beauty/appointments/updateappointment.html',None)
def deleteAppointment(request):
    return render(request, 'beauty/appointments/deleteappointment.html',None)

def appointments(request):
    list_appointments = Appointment.objects.all()
    context = {'list_appointments':list_appointments}
    return render(request, 'beauty/appointments/appointments.html', context)

class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer

class EmployeeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer

class AppointmentListAPIView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentCreateAPIView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=timezone.now())

class AppointmentDetailAPIView(RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDeleteAPIView(DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
