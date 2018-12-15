from django.urls import path

from . import views

urlpatterns = [
    path('<int:employee_id>/addEmployee/',views.addEmployee, name='addEmployee'),
    path('appointments/', views.appointments, name='appointments'),
]