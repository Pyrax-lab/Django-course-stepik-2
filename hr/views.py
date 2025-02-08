from django.shortcuts import render

# Create your views here.

from .models import Employee, Contact, Department

def main(request):
    employee = Employee.objects.filter(first_name = "Floppy")
    return render(request, "list.html", context={"employee" : employee})