from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from carpenter import models
from carpenter.forms import NewCp
from django.urls import reverse
# Create your views here.

def showList(request):
    employee = models.carpenter.objects.all()

    res = render(request,'employee/employees.html',{'employee': employee,'category':'carpenter'})
    return res

def addList(request):
    form = NewCp()
    res = render(request,'employee/new-employee.html',{'form':form,'category':'carpenter'})
    return res

def add(request):
    if request.method=='POST':
        form = NewCp(request.POST)
        cp = models.carpenter()
        cp.name = form.data['name']
        cp.state = form.data['state']
        cp.dist = form.data['dist']
        cp.phone = form.data['phone']
        cp.pincode = form.data['pincode']
        cp.experience = form.data['experience']
        cp.fee = form.data['fee']
        cp.save()
    return HttpResponseRedirect(reverse('carpenter-list'))


def editList(request):
    employee = models.carpenter.objects.get(id=request.GET['id'])
    fields = {'name':employee.name,
        'state':employee.state,
        'dist':employee.dist,
        'phone':employee.phone,
        'pincode':employee.pincode,
        'experience':employee.experience,
        'fee':employee.fee
        }
    form = NewCp(initial=fields)
    res = render(request,'employee/edit-list.html',{'form': form, 'employee': employee,'category':'carpenter'})
    return res

def edit(request):
    if request.method=='POST':
        form = NewCp(request.POST)
        employee = models.carpenter()
        employee.id = request.POST['id']
        employee.name = form.data['name']
        employee.state = form.data['state']
        employee.dist = form.data['dist']
        employee.phone = form.data['phone']
        employee.pincode = form.data['pincode']
        employee.experience = form.data['experience']
        employee.fee = form.data['fee']
        employee.save()
    return HttpResponseRedirect(reverse('carpenter-list'))

def deleteList(request):
    employeeId = request.GET['id']
    employee = models.carpenter.objects.filter(id=employeeId)
    employee.delete()
    return HttpResponseRedirect(reverse('carpenter-list'))

def viewProfile(request):
    employeeId = request.GET['id']
    employee = models.carpenter.objects.get(id=employeeId)
    res = render(request,'carpenter/viewProfile.html',{'employee':employee})
    return res
