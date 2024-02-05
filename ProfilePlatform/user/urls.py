from django.urls import path
from .import views

app_name = 'user'

urlpatterns =[
    path('register/',views.register_view, name='register_view'),
    path('login/',views.log_in_view,name ='log_in_view'),
    path('logout/',views.logout_view,name='logout_view')
]