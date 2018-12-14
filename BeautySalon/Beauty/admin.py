from django.contrib import admin

from .models import Employee, Appointment

admin.site.register(Employee)
admin.site.register(Appointment)