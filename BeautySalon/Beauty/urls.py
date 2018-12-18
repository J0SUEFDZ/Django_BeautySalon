from django.urls import path

from Beauty import views

urlpatterns = [
    path('addEmployee/<str:employee_name>/',views.addEmployee, name='addEmployee'),
    path('appointments/', views.AppointmentListAPIView.as_view(), name='appointments_list'),
    path('appointments/create/', views.AppointmentCreateAPIView.as_view(), name='appointments_create'),
    path('appointments/<str:pk>/', views.AppointmentDetailAPIView.as_view(), name='appointments_detail'),
    path('appointments/update/<str:pk>/', views.AppointmentUpdateAPIView.as_view(), name='appointments_update'),
    path('appointments/delete/<str:pk>/', views.AppointmentDeleteAPIView.as_view(), name='appointments_delete'),
    #path('employees/', views.employees, name='employees'),
    path('appointments/addappointment/', views.addAppointment, name='addappointment'),
    path('appointments/deleteappointment/', views.deleteAppointment, name='deleteappointment'),
    path('appointments/updateappointment/', views.updateAppointment, name='updateappointment'),
    path('employees/', views.EmployeeListAPIView.as_view(), name='employee_list'),
    path('employees/create/', views.EmployeeCreateAPIView.as_view(), name='employee_create'),
    path('employees/update/<int:pk>', views.EmployeeUpdateAPIView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>', views.EmployeeDeleteAPIView.as_view(), name='employee_delete'),
    path('employees/<int:pk>', views.EmployeeDetailAPIView.as_view(), name='employee_detail'),
]