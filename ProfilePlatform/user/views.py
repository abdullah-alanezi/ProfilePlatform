from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .models import Education,Skill, Profile
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


def update_profile(request:HttpRequest,user_id):
    user = User.objects.get(id=user_id)
    try:

        profile = user.profile
    except:
        profile = Profile(user=user)
    
    if request.user.is_authenticated and user.id == request.user.id:

        if request.method == 'POST':
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
            profile.bio = request.POST['bio']
            profile.career = request.POST['career']
            profile.linkedin = request.POST['linkedin']
            profile.github = request.POST['github']
            profile.save()

            return redirect('main:profile_view',user_id)
    
    return render(request,'user/update_profile.html')


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
    

def delete_education_view(request:HttpRequest,education_id):
    
    education = Education.objects.get(id = education_id)
    if request.user.is_authenticated:
        

        education.delete()
        return redirect('main:profile_view',request.user.id)





def add_skill(request:HttpRequest):

    user = request.user
    skill = Skill(user=user)
    if request.method == 'POST':
        proficiency_rate_to_int =int(request.POST['proficiency_rate'])
        skill.skill=request.POST['skill']
        skill.proficiency_rate= proficiency_rate_to_int
        skill.save()
        
        return redirect('main:profile_view',user.id)
    
def delete_skill(request:HttpRequest):
    if request.method == 'POST':
        skill_id = request.POST['skill']
        
        skill = Skill.objects.get(id=skill_id)

        if request.user.is_authenticated:

         skill.delete()

    return redirect('main:profile_view',request.user.id)
