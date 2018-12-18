from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    )
from Beauty.models import Employee, Appointment

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
        ]

class EmployeeCreateSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'name',
        ]

class AppointmentSerializer(ModelSerializer):
    employee_id = SerializerMethodField()
    class Meta:
        model = Appointment
        fields = [
            'id',
            'created_at',
            'date',
            'employee_id',
        ]
    def get_employee_id(self, obj):
        return str(obj.employee.name)

class AppointmentCreateSerializer(ModelSerializer):
    employee_obj = EmployeeSerializer(required=False,read_only=True)
    class Meta:
        model = Appointment
        fields = [
            'employee',
            'employee_obj',
            'date',
        ]
    
    def get_employee_id(self, obj):
        return str(obj.employee.name)



