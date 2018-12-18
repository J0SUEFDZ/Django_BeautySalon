from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=50)