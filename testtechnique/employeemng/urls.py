from django.urls import path
from . import views

urlpatterns = [
    path('<int:employee_id>/', views.get_employee, name='employeedetails'),
    path('list/', views.get_employees, name='employees'),
    path('add/', views.add_employee, name='addemployee'),
]
