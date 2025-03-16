from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url="login")
def home(request):
    if request.user.groups.filter(name="Admin"):
        return render(request,'home.html')
    current_date_formatted = datetime.now().strftime("%Y-%m-%d")
    bookuser=foodbook.objects.filter(user =request.user)
    data=bookuser.filter(date=current_date_formatted)
    return render(request,'home.html',{'data1':data})
    

def Loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            welmes = f"Welcome {request.user.username}"
            messages.info(request, welmes)
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password")
            return render(request, 'login.html')
    return render(request, 'login.html')


@login_required(login_url="login")
def book1(request):
    if request.method =="POST":
        form=contactform(request.POST)
        if form.is_valid():
            c=form.save(commit=False)
            c.user = request.user
            messages.success(request,"Your request has ben sent successfully")
            c.save()
            return redirect('home')
    return render(request,'help.html')


@login_required(login_url="login")
def feedbackuser(request):
    if request.method =="POST":
        form = feed(request.POST)
        if form.is_valid():
            c=form.save(commit=False)
            c.user = request.user
            c.save()
            messages.success(request,"Your request has ben sent successfully")
            return redirect("home")
    return render(request,"feedback.html")


@login_required(login_url="login")
def foodbookuser(request):
    if request.user.groups.filter(name="Admin"):
        if request.method =="POST":
            form=food(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                user_instance = User.objects.get(username=request.POST.get('name'))
                c.user = user_instance
                c.save()
                messages.success(request,"Your meal has ben booked successfully")
                return redirect("home")
    if request.method =="POST":
        form=food(request.POST)
        if form.is_valid():
            c=form.save(commit=False)
            c.user = request.user
            c.save()
            messages.success(request,"Your meal has ben booked successfully")
            return redirect("home")
    if request.user.groups.filter(name="Admin"):
        user=User.objects.all
        current_date_formatted = datetime.now().strftime("%Y-%m-%d")
        dic_data={
            'user':user,
            'date':current_date_formatted
        }
        return render(request,"foodbook.html",{"date":dic_data})
    current_date_formatted = datetime.now().strftime("%Y-%m-%d")
    return render(request,"foodbook.html",{"date":current_date_formatted})


@login_required(login_url="login")
def booklist(request):
    current_date_formatted = datetime.now().strftime("%Y-%m-%d")
    if request.user.groups.filter(name="Admin"):
        data=foodbook.objects.filter(date = current_date_formatted)
        lenth=len(data)
        dic_data={
            'date':data,
            'length':lenth,
        }
        return render(request,"booklist.html",{"dic_data": dic_data})
    data=foodbook.objects.filter(user = request.user)
    confirmdata=data.filter(date = current_date_formatted)
    return render(request,"booklist.html",{"dic_data": confirmdata})

    
@login_required(login_url="login")
def deleteuser(request,id):
    customer = get_object_or_404(foodbook, id=id)
    customer.delete()
    messages.success(request,"Your meal has ben canceled successfully")
    return redirect('booklist')


@login_required(login_url="login")
def Logoutuser(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def feedbacklist(request):
    if request.user.groups.filter(name="Admin"):
        return render(request,"feedbacklist.html",{'dic_data':feedback.objects.all()})
    return render(request,"feedbacklist.html")

@login_required(login_url="login")
def helplist(request):
    if request.user.groups.filter(name="Admin"):
        return render(request,"helplist.html",{'dic_data':contact.objects.all()})
    return render(request,"helplist.html")

@login_required(login_url="login")
def helpview(request,id):
    return render(request,"helpview.html",{'data':get_object_or_404(contact,id=id)})

@login_required(login_url="login")
def feedbackview(request,id):
    return render(request,"feedbackview.html",{'data':get_object_or_404(feedback,id=id)})