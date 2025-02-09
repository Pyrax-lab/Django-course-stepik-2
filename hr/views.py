from django.shortcuts import render

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

   
    count_employee = len(employee)

    
    return render(request, "list.html", context={"employee" : employee, "count": count_employee})



# Без индексирования 
#2406 1955 1851   A = 191, 174, 173   J = 302, 272, 274
#C индексирования 
# 1913 1895 1855  A = 189 170 172      J = 306 276  271