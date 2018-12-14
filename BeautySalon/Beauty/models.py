from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)

class Appointment(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    created_at = models.DateTimeField('Creation of the appointment')
    date = models.DateTimeField('Date of the appointment')


