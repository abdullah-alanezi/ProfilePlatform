from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .models import Education
# Create your views here.


def register_view(request:HttpRequest):
    if request.method == 'POST':
        user =User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        user.save()
        return redirect('main:home_view')
    return render(request,'user/register.html')




def log_in_view(request:HttpRequest):
    msg=None
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user = authenticate(username =request.POST['username'],password = request.POST['password'])

            if user:
                login(request,user)
                return redirect('main:home_view')
            else:
                msg="please inter correct username and password"
    else:
        return redirect('main:home_view')
    return render(request,'user/login.html',{'msg':msg})


def logout_view(request:HttpRequest):

    if request.user.is_authenticated:
        logout(request)
        return redirect('user:log_in_view')


def add_education(request:HttpRequest):

    user = request.user
    education = Education(user = user)

    if request.method == 'POST':
        education.qualification = request.POST['qualification']
        education.start_year = request.POST['start_year']
        education.end_year = request.POST['end_year']
        education.specialization = request.POST['specialization']
        education.university_name = request.POST['university_name']
        education.save()

        return redirect('main:profile_view',user.id)