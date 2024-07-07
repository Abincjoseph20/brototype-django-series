from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def loggin(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']  
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('list')  
        else:
            error_message='invalid user!'
    return render(request,'usersapp/login.html',{'error_message':error_message})


def loggout(request):
    logout(request)
    return redirect('login')  

def signup(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        try:
             user=User.objects.create_user(username=username,password=password) #custome User padikkan onde
        except Exception as e:
            error_message=str(e)
    return render(request,'usersapp/signup.html',{'user':user,'error_message':error_message})

