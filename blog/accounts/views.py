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
                return render(request,'register.html',{'error':"User already eist"})

            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
            return redirect('home')
        else:
            return render(request,'register.html',{'error':"Password don't match"})

    else:   
        return render(request, 'register.html')


