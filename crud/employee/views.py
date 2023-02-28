from django.shortcuts import render, redirect
from employee.forms import EmployeeForm,LoginForm
from employee.models import Employee
from django.contrib.auth import login,authenticate
from django.contrib import messages

def login_page(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is  not None:
                login(request,user)
                return redirect("/show/")
            else:
                messages.error(request,"Username or Password is invalid")
                return redirect("login")
    return render(request,"login.html",context={"form":form})

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})

def add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show/')
    else:
        form = EmployeeForm()
    return render(request,'add.html',{'form':form})

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():  
        form.save()  
        return redirect("/show/")
    return render(request, 'edit.html', {'employee': employee})

def delete(request, id):
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show/")