from django.urls import path
from .import views

app_name = 'user'

urlpatterns =[
    path('register/',views.register_view, name='register_view'),
    path('login/',views.log_in_view,name ='log_in_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('add/education',views.add_education,name= 'add_education'),
    path('add/skill/',views.add_skill,name='add_skill'),
    path('update/profile/<user_id>/',views.update_profile,name='update_profile'),
    path('delete/education/<education_id>/',views.delete_education_view,name='delete_education_view'),
    path('delete/skill/',views.delete_skill, name='delete_skill'),
    path("contact/",views.contact_view,name="contact_view"),
]