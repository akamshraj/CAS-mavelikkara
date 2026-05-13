

from django.shortcuts import render
from .models import Department

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')# Create your views here.



def department_view(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})
from django.shortcuts import render
from .models import HOD

def departmentdetails(request):
    hods = HOD.objects.all()
    return render(request, 'departmentdetails.html', {'hods': hods})