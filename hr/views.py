from django.shortcuts import render
from django.contrib.auth.models import Permission

# Create your views here.

from .models import Employee, Contact, Department

def main(request):
    
    filtr = ''
    if request.method == "GET":
        #print(request.GET.get("tt"))
        filtr = request.GET.get("tt")


    if filtr == None:
        employee = Employee.objects.all()
    else:
        employee = Employee.objects.filter(first_name = filtr)

    #print('blog.add_post' in request.user.get_all_permissions())
    print(Permission.objects.all())# так можем посмотреть все рарешения которые есть в проекте
    count_employee = len(employee)

    
    return render(request, "list.html", context={"employee" : employee, "count": count_employee})


