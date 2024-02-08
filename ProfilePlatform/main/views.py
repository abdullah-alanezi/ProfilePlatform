from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from user.models import Skill,Education
# Create your views here.



def home_view(request:HttpRequest):

    return render(request,'main/home.html')

def profile_view(request:HttpRequest,user_id):

    user = User.objects.get(id=user_id)
    skills = Skill.objects.filter(user = user)
    return render(request,'main/profile.html',{'user':user,'skills':skills})
