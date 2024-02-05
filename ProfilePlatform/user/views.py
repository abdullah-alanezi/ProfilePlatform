from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
# Create your views here.


def register_view(request:HttpRequest):
    if request.method == 'POST':
        user =User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        user.save()
        return redirect('main:profile_view')
    return render(request,'user/register.html')




def log_in_view(request:HttpRequest):
    msg=None
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user = authenticate(username =request.POST['username'],password = request.POST['password'])

            if user:
                login(request,user)
                return redirect('main:profile_view')
            else:
                msg="please inter correct username and password"
    else:
        return redirect('main:profile_view')
    return render(request,'user/login.html',{'msg':msg})


def logout_view(request:HttpRequest):

    if request.user.is_authenticated:
        logout(request)
        return redirect('user:log_in_view')