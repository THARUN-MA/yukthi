from django.shortcuts import render,redirect
from th.models import userdetail,actordetail,consultdetail,modeldetail,dancerdetail,singerdetail
# Create your views here.
def index(request):
    request.session['usr']=""
    request.session['usrtype']=""
    return render(request,'index.html')

def signup(request):
    # if request.method=="POST":
    #     if request.FILES['myfile']:
    #         if not (actordetail.objects.filter(email=request.POST['email']).exists()):
    #             psp="0"
    #             try:
    #                 if request.POST['webseries']:
    #                     web="1"
    #             except:
    #                 web="0"
    #             try:
    #                 if request.POST['serial']:
    #                     ser="1"
    #             except:
    #                 ser="0"
    #             try:
    #                 if request.POST['movies']:
    #                     mov="1"
    #             except:
    #                 mov="0"
    #             try:
    #                 if request.POST['shortmovies']:
    #                     shmov="1"
    #             except:
    #                 shmov="0"
    #             try:
    #                 print('TRY')
    #                 if request.POST['passport']:
    #                     print('TRYs')
    #                     psp="1"
    #             except:
    #                 print('TRYF')
    #                 psp="0"
    #             actordetail(email=request.POST['email'],name=request.POST['name1'],password=request.POST['pass'],dob=request.POST['dob'],age=request.POST['age'],mobile=request.POST['Mobile_Number'],gender=request.POST['Gender'],address=request.POST['Address'],city=request.POST['City'],pin=request.POST['Pin_Code'],state=request.POST['State'],country=request.POST['Country'],webseries=web,serial=ser,movies=mov,shortmovies=shmov,experience=request.POST['experience'],haircolor=request.POST['haircolor'],skincolor=request.POST['skincolor'],passport=psp,profilepic=request.FILES['myfile']).save()
    #             return redirect('th:login')
    return render(request,'signup.html')

# def actorsignup(request)

def actorsign(request):
    if request.method=="POST":
        if request.FILES['myfile']:
            if not (actordetail.objects.filter(email=request.POST['email']).exists()):
                psp="0"
                try:
                    if request.POST['webseries']:
                        web="1"
                except:
                    web="0"
                try:
                    if request.POST['serial']:
                        ser="1"
                except:
                    ser="0"
                try:
                    if request.POST['movies']:
                        mov="1"
                except:
                    mov="0"
                try:
                    if request.POST['shortmovies']:
                        shmov="1"
                except:
                    shmov="0"
                try:
                    print('TRY')
                    if request.POST['passport']:
                        print('TRYs')
                        psp="1"
                except:
                    print('TRYF')
                    psp="0"
                actordetail(email=request.POST['email'],name=request.POST['name1'],password=request.POST['pass'],dob=request.POST['dob'],age=request.POST['age'],mobile=request.POST['Mobile_Number'],gender=request.POST['Gender'],address=request.POST['Address'],city=request.POST['City'],pin=request.POST['Pin_Code'],state=request.POST['State'],country=request.POST['Country'],webseries=web,serial=ser,movies=mov,shortmovies=shmov,experience=request.POST['experience'],haircolor=request.POST['haircolor'],skincolor=request.POST['skincolor'],passport=psp,profilepic=request.FILES['myfile']).save()
                return redirect('th:login')
    return render(request,'actorsign.html')


def modelsign(request):
    if request.method=="POST":
        if request.FILES['myfile']:
            if not (modeldetail.objects.filter(email=request.POST['email']).exists()):
                psp="0"
                try:
                    if request.POST['catalog']:
                        cat="1"
                except:
                    cat="0"
                try:
                    if request.POST['hoarding']:
                        hor="1"
                except:
                    hor="0"
                try:
                    if request.POST['mrmrs']:
                        mrms="1"
                except:
                    mrms="0"
                try:
                    if request.POST['des_rmp']:
                        dsmp="1"
                except:
                    dsmp="0"
                try:
                    print('TRY')
                    if request.POST['passport']:
                        print('TRYs')
                        psp="1"
                except:
                    print('TRYF')
                    psp="0"
                modeldetail(email=request.POST['email'],name=request.POST['name1'],password=request.POST['pass'],dob=request.POST['dob'],age=request.POST['age'],mobile=request.POST['Mobile_Number'],gender=request.POST['Gender'],address=request.POST['Address'],city=request.POST['City'],pin=request.POST['Pin_Code'],state=request.POST['State'],country=request.POST['Country'],catalog=cat,hoarding=hor,mrmrs=mrms,des_rmp=dsmp,experience=request.POST['experience'],haircolor=request.POST['haircolor'],skincolor=request.POST['skincolor'],passport=psp,profilepic=request.FILES['myfile']).save()
                return redirect('th:login')
    return render(request,'modelsign.html')



def dancersign(request):
    if request.method=="POST":
        if request.FILES['myfile']:
            if not (dancerdetail.objects.filter(email=request.POST['email']).exists()):
                psp="0"
                try:
                    if request.POST['bara']:
                        bar="1"
                except:
                    bar="0"
                try:
                    if request.POST['free']:
                        fre="1"
                except:
                    fre="0"
                try:
                    if request.POST['side']:
                        sid="1"
                except:
                    sid="0"
                try:
                    if request.POST['dsr']:
                        ds="1"
                except:
                    ds="0"
                try:
                    print('TRY')
                    if request.POST['passport']:
                        print('TRYs')
                        psp="1"
                except:
                    print('TRYF')
                    psp="0"
                dancerdetail(email=request.POST['email'],name=request.POST['name1'],password=request.POST['pass'],dob=request.POST['dob'],age=request.POST['age'],mobile=request.POST['Mobile_Number'],gender=request.POST['Gender'],address=request.POST['Address'],city=request.POST['City'],pin=request.POST['Pin_Code'],state=request.POST['State'],country=request.POST['Country'],barathanatyam=bar,freestyle=fre,sidedancer=sid,danceshow=ds,experience=request.POST['experience'],haircolor=request.POST['haircolor'],skincolor=request.POST['skincolor'],passport=psp,profilepic=request.FILES['myfile']).save()
                return redirect('th:login')
    return render(request,'dancersign.html')


def singersign(request):
    if request.method=="POST":
        if request.FILES['myfile']:
            if not (singerdetail.objects.filter(email=request.POST['email']).exists()):
                psp="0"
                try:
                    if request.POST['movie']:
                        mov="1"
                except:
                    mov="0"
                try:
                    if request.POST['serial']:
                        ser="1"
                except:
                    ser="0"
                try:
                    print('TRY')
                    if request.POST['passport']:
                        print('TRYs')
                        psp="1"
                except:
                    print('TRYF')
                    psp="0"
                singerdetail(email=request.POST['email'],name=request.POST['name1'],password=request.POST['pass'],dob=request.POST['dob'],age=request.POST['age'],mobile=request.POST['Mobile_Number'],gender=request.POST['Gender'],address=request.POST['Address'],city=request.POST['City'],pin=request.POST['Pin_Code'],state=request.POST['State'],country=request.POST['Country'],movie=mov,serial=ser,experience=request.POST['experience'],haircolor=request.POST['haircolor'],skincolor=request.POST['skincolor'],passport=psp,profilepic=request.FILES['myfile']).save()
                return redirect('th:login')
    return render(request,'singersign.html')


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
