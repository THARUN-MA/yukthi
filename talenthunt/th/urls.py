from django.conf.urls import url,include
from th import views

app_name='th'

urlpatterns=[
    url('login/',views.login,name='login'),
    url('signup/',views.signup,name='signup'),
    url('logout/',views.logout,name='logout'),
    url('consultdashboard/',views.consultdashboard,name='consultdashboard'),
    url('actordashboard/',views.actordashboard,name='actordashboard'),
    url('singerdashboard/',views.singerdashboard,name='singerdashboard'),
    url('dancerdashboard/',views.dancerdashboard,name='dancerdashboard'),
    url('modeldashboard/',views.modeldashboard,name='modeldashboard'),
    url('dashboard/',views.dashboard,name='dashboard'),
    url('admindash/',views.admindash,name='admindash'),
    url('actorsign/',views.actorsign,name='actorsign'),
    url('singersign/',views.singersign,name='singersign'),
    url('dancersign/',views.dancersign,name='dancersign'),
    url('modelsign/',views.modelsign,name='modelsign'),
    url('consultsign/',views.consultsign,name='consultsign'),
    url('enrolladd/(?P<value>\w+)$',views.enrolladd,name='enrolladd'),
    url('createaudtion/',views.createaudtion,name='createaudtion'),
    url('manageaudtion/',views.manageaudtion,name='manageaudtion'),
    url('createsinger/',views.createsinger,name='createsinger'),
    url('createactor/',views.createactor,name='createactor'),
    url('createmodel/',views.createmodel,name='createmodel'),
    url('createdancer/',views.createdancer,name='createdancer'),
    url('enroll/(?P<value>\w+)$',views.enroll,name='enroll'),
    url('manage2/(?P<value>\w+)$',views.manage2,name='manage2'),

]
