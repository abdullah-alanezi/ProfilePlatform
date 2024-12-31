from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to='images/',default='images/default.jpg')
    phone_number = models.IntegerField(default=0)
    bio = models.TextField()
    career = models.CharField(max_length=255)
    linkedin = models.URLField()
    github = models.URLField()

    def __str__(self) -> str:
        return self.user.username



class Education(models.Model):

    user = models.ForeignKey(User,on_delete = models.CASCADE)
    qualifications = models.TextChoices('qualifications',['None','Diploma','Bachelor','Doctorate'])
    qualification = models.CharField(max_length=56,choices = qualifications.choices, default='None')
    start_year = models.DateField()
    end_year = models.DateField()
    specialization = models.CharField(max_length = 255)
    university_name = models.CharField(max_length = 255)


    def __str__(self) -> str:
        return self.user.username

class Skill(models.Model):

    user = models.ForeignKey(User,on_delete = models.CASCADE)
    skill = models.CharField(max_length = 255)
    proficiency_rate =models.IntegerField()

    

    def __str__(self) -> str:
        return self.user.username
    



class Course(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    hour = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
