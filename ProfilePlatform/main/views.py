from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from user.models import Skill,Education
# Create your views here.

def profile_view(request:HttpRequest):

    user = User.objects.get(id= request.user.id)
    skills = Skill.objects.filter(user = user)
    return render(request,'main/profile.html',{'user':user,'skills':skills})
