from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    created_at = models.DateField('Creation of the appointment')
    date = models.DateField('Date of the appointment')

    def __str__(self):
        return str(self.date)+" with "+self.employee.name

