from django.shortcuts import render,redirect
from EmployeeApp.models import Emp
from django.http import HttpResponse
from Employeeproject import settings

# Create your views here.
def loadMe(request):
    return render(request,'./templates/RegForm.html')

# insert operation
def crudops(request):
    # create an entry
        emp=Emp(
        emp_id=request.GET['empid'],
        emp_name=request.GET['empname'],
        emp_salary=request.GET['empsalary']
        )
        emp.save()
        return redirect('../viewAll')
        
# select operation
def viewAll(request):
    objs=Emp.objects.all()
    root="<table border='1'><tr><th>ID</th><th>Emp id</th><th>Employee name</th><th>Employee salary</th></tr>"
    res=" "
    for cl in objs:
        res=res+"<tr><td>"+str(cl.id)+"</td><td>"+cl.Emp_id+"</td><td>"+cl.Emp_name+"</td><td>"+cl.Emp_salary+"</tr>"
    root=root+""+res+"</table>"
    root=root+"<a href='../loadMe'>Back</a>"
    return HttpResponse(root)


# select by condition
def filterByid(request,id):
    objs=Emp.objects.filter(Emp_id=id)
    res="<br/>"
    for cl in objs:
        res=res+cl.Emp_name+" "+cl.Emp_salary+"<br/>"
    return HttpResponse(res)

# Deletion of records
def delStud(request,name):
    emp=Emp.objects.get(Emp_name=name)
    emp.delete()
    return redirect('../viewAll')



