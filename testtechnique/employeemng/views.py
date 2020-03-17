from django.shortcuts import render
from .models import Employee, EmployeeForm
from django.http import Http404
# Create your views here.


def get_employees(request):
    return render(
        request, "employee/employees.html", {
            "employees": Employee.objects.all()
        }
    )


def get_employee(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404("Question does not exist")
    return render(
        request, 'employee/employeedetails.html', {
            'employee': employee
        }
    )


def add_employee(request):
    context = {}
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            function = form.cleaned_data.get("function")
            avatar = form.cleaned_data.get("avatar")
            birthday = form.cleaned_data.get("birthday")
            obj = Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                function=function,
                avatar=avatar,
                birthday=birthday
            )
            obj.save()
            print(obj)
    else:
        form = EmployeeForm()
    context['form'] = form
    return render(request, "employee/addemployee.html", context)
