from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

def home(request):
    return render(request, 'login.html')

def signup(request):
    if request.method== "POST" : 
        # return render(request,'register.html')
        u1=request.POST['password']
        u2=request.POST['password_']
        if u1==u2:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'register.html',{'error':"Username already eist"})

            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                # auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'register.html',{'error':"Password don't match"})

    else:   
        return render(request, 'register.html')

def login(request):
    if request.method=="POST":
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'showBlog.html')
        else:
            return render(request,'login.html',{'error':'Invalid login credentials'})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect(home)