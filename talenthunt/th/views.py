from django.shortcuts import render,redirect
from th.models import userdetail,actordetail,consultdetail
# Create your views here.
def index(request):
    request.session['usr']=""
    request.session['usrtype']=""
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        if request.POST['opt']=='usr':
            if request.POST['your-email']=='admin@gmail.com' or userdetail.objects.filter(email=request.POST['your-email']).exists():
                return redirect('th:signup')
            else:
                userdetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password']).save()
                return redirect('th:login')
        elif request.POST['opt']=='act':
            if request.POST['your-email']=='admin@gmail.com' or actordetail.objects.filter(email=request.POST['your-email']).exists():
                return redirect('th:signup')
            else:
                actordetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password']).save()
                return redirect('th:login')
        elif request.POST['opt']=='con':
            if request.POST['your-email']=='admin@gmail.com' or consultdetail.objects.filter(email=request.POST['your-email']).exists():
                return redirect('th:signup')
            else:
                consultdetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password']).save()
                return redirect('th:login')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        if request.POST['ch']=='admin':
            if (request.POST['inputEmail']=='admin@gmail.com' and request.POST['inputPassword']=='@1geniUs'):
                request.session['usrtype']='admin'
                request.session['usr']='admin'
                return redirect('th:admindash')
        elif request.POST['ch']=='usr':
            if userdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
                    request.session['usr']=request.POST['inputEmail']
                    request.session['usrtype']='usr'
                    return redirect('th:dashboard')
        elif request.POST['ch']=='act':
            if actordetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
                    request.session['usr']=request.POST['inputEmail']
                    request.session['usrtype']='act'
                    return redirect('th:actordashboard')
        elif request.POST['ch']=='con':
            if consultdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
                    request.session['usr']=request.POST['inputEmail']
                    request.session['usrtype']='con'
                    print(request.session['usrtype'])
                    print(request.session['usr'])
                    return redirect('th:consultdashboard')
        else:
            print('NO')
            return redirect('th:login')
    return render(request,'login.html')



def logout(request):
    request.session['usr']=""
    request.session['usrtype']=""
    return render(request,'index.html')

def dashboard(request):
    if (request.session['usr'] and request.session['usrtype']=='usr'):
        return render(request,'dashboard.html')
    else:
        return redirect('th:login')

def actordashboard(request):
    print('s1')
    if (request.session['usr'] and request.session['usrtype']=='act'):
        print('s1')
        return render(request,'actordashboard.html')
    else:
        return redirect('th:login')

def consultdashboard(request):
    if (request.session['usr'] and request.session['usrtype']=='con'):
        return render(request,'consultdashboard.html')
    else:
        return redirect('th:login')

def admindash(request):
    if (request.session['usrtype']=='admin' and request.session['usr']=='admin'):
        return render(request,'admin.html')
    else:
        return redirect('th:login')
