from django.conf.urls import url,include
from th import views

app_name='th'

urlpatterns=[
    url('login/',views.login,name='login'),
    url('signup/',views.signup,name='signup'),
    url('logout/',views.logout,name='logout'),
    url('consultdashboard/',views.consultdashboard,name='consultdashboard'),
    url('actordashboard/',views.actordashboard,name='actordashboard'),
    url('dashboard/',views.dashboard,name='dashboard'),
    url('admindash/',views.admindash,name='admindash'),
    url('actorsign/',views.actorsign,name='actorsign'),
    url('singersign/',views.singersign,name='singersign'),
    url('dancersign/',views.dancersign,name='dancersign'),
    url('modelsign/',views.modelsign,name='modelsign'),
]
