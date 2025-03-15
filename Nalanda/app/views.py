from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'home.html')

def Loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password")
            return render(request, 'login.html')
    return render(request, 'login.html')

def book1(request):
    if request.method =="POST":
        form=contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'help.html')

def feedbackuser(request):
    if request.method =="POST":
        form = feed(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,"feedback.html")
def foodbookuser(request):
    if request.method =="POST":
        form=food(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    current_date_formatted = datetime.now().strftime("%Y-%m-%d")
    return render(request,"foodbook.html",{"date":current_date_formatted})
def booklist(request):
    current_date_formatted = datetime.now().strftime("%Y-%m-%d")
    data=foodbook.objects.filter(date = current_date_formatted)
    lenth=len(data)
    dic_data={
        'date':data,
        'length':lenth,
    }
    return render(request,"booklist.html",{"dic_data": dic_data})

def deleteuser(request,id):
    customer = get_object_or_404(foodbook, id=id)
    customer.delete()
    return redirect('booklist')
def Logoutuser(request):
    logout(request)
    return redirect("login")