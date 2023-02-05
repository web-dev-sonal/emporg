from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from driver import models
from driver.forms import NewDriver
from django.urls import reverse
# Create your views here.

def showList(request):
    employee = models.driver.objects.all()
    #username = request.session['username']
    res = render(request,'employee/employees.html',{'employee': employee,'category':'driver'})
    return res

def addList(request):
    form = NewDriver()
    res = render(request,'employee/new-employee.html',{'form':form,'category':'driver'})
    return res

def add(request):
    if request.method=='POST':
        form = NewDriver(request.POST)
        cp = models.driver()
        cp.name = form.data['name']
        cp.state = form.data['state']
        cp.dist = form.data['dist']
        cp.phone = form.data['phone']
        cp.pincode = form.data['pincode']
        cp.experience = form.data['experience']
        cp.fee = form.data['fee']
        cp.vehicle = form.data['vehicle']
        cp.save()
    return HttpResponseRedirect('driver-list')

def editList(request):
    employee = models.driver.objects.get(id=request.GET['id'])
    fields = {'name':employee.name,
        'state':employee.state,
        'dist':employee.dist,
        'phone':employee.phone,
        'pincode':employee.pincode,
        'experience':employee.experience,
        'fee':employee.fee,
        'vehicle':employee.vehicle
        }
    form = NewDriver(initial=fields)
    return HttpResponseRedirect(reverse('driver-list'))

def edit(request):
    if request.method=='POST':
        form = NewDriver(request.POST)
        employee = models.driver()
        employee.id = request.POST['id']
        employee.name = form.data['name']
        employee.state = form.data['state']
        employee.dist = form.data['dist']
        employee.phone = form.data['phone']
        employee.pincode = form.data['pincode']
        employee.experience = form.data['experience']
        employee.fee = form.data['fee']
        employee.vehicle = form.data['vehicle']
        employee.save()
    return HttpResponseRedirect(reverse('driver-list'))

def deleteList(request):
    employeeId = request.GET['id']
    employee = models.driver.objects.filter(id=employeeId)
    employee.delete()
    return HttpResponseRedirect(reverse('driver-list'))

def viewProfile(request):
    employeeId = request.GET['id']
    employee = models.driver.objects.get(id=employeeId)
    res = render(request,'driver/viewProfile.html',{'employee':employee})
    return res
