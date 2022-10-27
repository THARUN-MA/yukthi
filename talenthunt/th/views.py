from django.shortcuts import render,redirect
from th.models import userdetail,actordetail,consultdetail,enrolled,modeldetail,dancerdetail,singerdetail,counter,createactord,createmodeld,createdancerd,createsingerd
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

def consultsign(request):
    if request.method=="POST":
        if not (consultdetail.objects.filter(email=request.POST['email']).exists()):
            consultdetail(email=request.POST['email'],name=request.POST['name1'],password=request.POST['pass'],cmpname=request.POST['cmpname'],mobile=request.POST['Mobile_Number'],address=request.POST['Address'],city=request.POST['City'],pin=request.POST['Pin_Code'],state=request.POST['State'],country=request.POST['Country']).save()
            return redirect('th:login')
    return render(request,'consultsign.html')


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
        elif request.POST['ch']=='dnc':
            if dancerdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
                    request.session['usr']=request.POST['inputEmail']
                    request.session['usrtype']='dnc'
                    return redirect('th:actordashboard')
        elif request.POST['ch']=='sng':
            if singerdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
                    request.session['usr']=request.POST['inputEmail']
                    request.session['usrtype']='sng'
                    print(request.session['usrtype'])
                    print(request.session['usr'])
                    return redirect('th:actordashboard')
        elif request.POST['ch']=='mdl':
            if modeldetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
                    request.session['usr']=request.POST['inputEmail']
                    request.session['usrtype']='mdl'
                    print(request.session['usrtype'])
                    print(request.session['usr'])
                    return redirect('th:actordashboard')
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
        context={}
        a=actordetail.objects.filter(email=request.session['usr'])
        if a[0].webseries=="1":
            context['data1']=createactord.objects.filter(webseries="1")
        if a[0].serial=="1":
            context['data2']=createactord.objects.filter(serial="1")
        if a[0].movies=="1":
            context['data3']=createactord.objects.filter(movies="1")
        if a[0].shortmovies=="1":
            context['data4']=createactord.objects.filter(shortmovies="1")
        return render(request,'actordashboard.html',context)
    elif (request.session['usr'] and request.session['usrtype']=='dnc'):
        context={}
        a=dancerdetail.objects.filter(email=request.session['usr'])
        if a[0].barathanatyam=="1":
            context['data1']=createdancerd.objects.filter(barathanatyam="1")
        if a[0].freestyle=="1":
            context['data2']=createdancerd.objects.filter(freestyle="1")
        if a[0].sidedancer=="1":
            context['data3']=createdancerd.objects.filter(sidedancer="1")
        if a[0].danceshow=="1":
            context['data4']=createdancerd.objects.filter(danceshow="1")
        return render(request,'dancerdashboard.html',context)
    elif (request.session['usr'] and request.session['usrtype']=='mdl'):
        context={}
        a=modeldetail.objects.filter(email=request.session['usr'])
        if a[0].catalog=="1":
            context['data1']=createmodeld.objects.filter(catalog="1")
        if a[0].hoarding=="1":
            context['data2']=createmodeld.objects.filter(hoarding="1")
        if a[0].mrmrs=="1":
            context['data3']=createmodeld.objects.filter(mrmrs="1")
        if a[0].des_rmp=="1":
            context['data4']=createmodeld.objects.filter(des_rmp="1")
        return render(request,'modeldashboard.html',context)
    elif (request.session['usr'] and request.session['usrtype']=='sng'):
        context={}
        a=singerdetail.objects.filter(email=request.session['usr'])
        if a[0].movie=="1":
            context['data1']=createsingerd.objects.filter(movie="1")
        if a[0].serial=="1":
            context['data2']=createsingerd.objects.filter(serial="1")
        return render(request,'singerdashboard.html',context)
    else:
        return redirect('th:login')

def enroll(request,value=None):
    if request.session['usr']:
        if request.session['usrtype']=="act":
            a=createactord.objects.filter(aid=value)
            b=False
            if enrolled.objects.filter(email=request.session['usr'],aid=value).exists():
                b=True
            if request.method=="POST":
                if request.FILES['myfile']:
                    enrolled(aid=value,files=request.FILES['myfile'],email=request.session['usr']).save()
                    return redirect('th:actordashboard')
        elif request.session['usrtype']=="dnc":
            a=createdancerd.objects.filter(aid=value)
            b=False
            if enrolled.objects.filter(email=request.session['usr'],aid=value).exists():
                b=True
            if request.method=="POST":
                if request.FILES['myfile']:
                    enrolled(aid=value,files=request.FILES['myfile'],email=request.session['usr']).save()
                    return redirect('th:dancerdashboard')
        elif request.session['usrtype']=="mdl":
            a=createmodeld.objects.filter(aid=value)
            b=False
            if enrolled.objects.filter(email=request.session['usr'],aid=value).exists():
                b=True
            if request.method=="POST":
                if request.FILES['myfile']:
                    enrolled(aid=value,files=request.FILES['myfile'],email=request.session['usr']).save()
                    return redirect('th:modeldashboard')
        elif request.session['usrtype']=="sng":
            a=createsingerd.objects.filter(aid=value)
            b=False
            if enrolled.objects.filter(email=request.session['usr'],aid=value).exists():
                b=True
            if request.method=="POST":
                if request.FILES['myfile']:
                    enrolled(aid=value,files=request.FILES['myfile'],email=request.session['usr']).save()
                    return redirect('th:singerdashboard')
        return render(request,'enroll.html',{'data':a[0],'enr':b})
    else:
        return redirect('th:login')


def enrolladd(request,value=None):
    if request.session['usr']:
        enrolled(aid=value,email=request.session['usr']).save()
        return redirect('th:actordashboard')
    else:
        return redirect('th:login')




def consultdashboard(request):
    if (request.session['usr'] and request.session['usrtype']=='con'):
        return render(request,'consultdashboard.html')
    else:
        return redirect('th:login')

def createaudtion(request):
    if (request.session['usr'] and request.session['usrtype']=='con'):
        return render(request,'createaudition.html')
    else:
        return redirect('th:login')

def createsinger(request):
    if (request.session['usr'] and request.session['usrtype']=='con'):
        if request.method=="POST":
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
            idd=counter.objects.all()
            createsingerd(aid=str(idd[0].iid),email=request.session['usr'],name=request.POST['name'],desc=request.POST['desc'],movie=mov,serial=ser).save()
            counter.objects.filter(iid=idd[0].iid).update(iid=str(int(idd[0].iid)+1))
            return redirect('th:consultdashboard')
        return render(request,'createsinger.html')
    else:
        return redirect('th:login')

def createactor(request):
    if (request.session['usr'] and request.session['usrtype']=='con'):
        if request.method=="POST":
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
            idd=counter.objects.all()
            createactord(aid=str(idd[0].iid),email=request.session['usr'],name=request.POST['name'],desc=request.POST['desc'],webseries=web,serial=ser,movies=mov,shortmovies=shmov).save()
            counter.objects.filter(iid=idd[0].iid).update(iid=str(int(idd[0].iid)+1))
            return redirect('th:consultdashboard')
        return render(request,'createactor.html')
    else:
        return redirect('th:login')




def createmodel(request):
    if (request.session['usr'] and request.session['usrtype']=='con'):
        if request.method=="POST":
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
            idd=counter.objects.all()
            createmodeld(aid=str(idd[0].iid),email=request.session['usr'],name=request.POST['name'],desc=request.POST['desc'],catalog=cat,hoarding=hor,mrmrs=mrms,des_rmp=dsmp).save()
            counter.objects.filter(iid=idd[0].iid).update(iid=str(int(idd[0].iid)+1))
            return redirect('th:consultdashboard')
        return render(request,'createmodel.html')
    else:
        return redirect('th:login')



def createdancer(request):
    if (request.session['usr'] and request.session['usrtype']=='con'):
        if request.method=="POST":
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
            idd=counter.objects.all()
            createdancerd(aid=str(idd[0].iid),email=request.session['usr'],name=request.POST['name'],desc=request.POST['desc'],barathanatyam=bar,freestyle=fre,sidedancer=sid,danceshow=ds).save()
            counter.objects.filter(iid=idd[0].iid).update(iid=str(int(idd[0].iid)+1))
            return redirect('th:consultdashboard')
        return render(request,'createdancer.html')
    else:
        return redirect('th:login')



def manageaudtion(request):
    if (request.session['usr'] and request.session['usrtype']=='con'):
        context={}
        context['actor']=createactord.objects.filter(email=request.session['usr'])
        context['dancer']=createdancerd.objects.filter(email=request.session['usr'])
        context['model']=createmodeld.objects.filter(email=request.session['usr'])
        context['singer']=createsingerd.objects.filter(email=request.session['usr'])
        return render(request,'manageaudtion.html',context)
    else:
        return redirect('th:login')


def manage2(request,value=None):
    if (request.session['usr'] and request.session['usrtype']=='con'):
        a=enrolled.objects.filter(aid=value)
        return render(request,'manage2.html',{'data':a})


def admindash(request):
    if (request.session['usrtype']=='admin' and request.session['usr']=='admin'):
        return render(request,'admin.html')
    else:
        return redirect('th:login')
