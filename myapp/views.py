from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib import messages
from .models import Feature,product,hospitals,reports,adhar,tempreports,pad
from django.core.mail import send_mail
from django.conf import settings
#from django.core.mail import send_mail
#import pywhatkit
# Create your views here.
kw=''
global capital,small,sc,nl
capital=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
small = list('abcdefghijklmnopqrstuvwxyz')
sc=list("@#₹_&/~`|•√π€¥$¢^%©®\!(){}[]")
nl=list('0123456789')
def home(request):
    return render(request,'home.html')
"""def index(request):
    o1=request.POST['op1']
    o2=request.POST['op2']
    o3=request.POST['op3']
    o4=request.POST['op4']
    features=Feature.objects.all()
    if request.user.is_authenticated()==True:
        username = request.user.username
        p=product.objects.filter(username=username)
        for i in p:
            i.op1=o1
            i.op2=o2
            i.op3=o3
            i.op4=o4
            i.save();
    else:
        return redirect('/')

    return render(request,'index.html',{'features':features})"""

"""def counter(request):
    ta=request.POST['text']
    t=len(ta.split())
    return render(request,'counter.html',{'t':t})"""
def signup(request):
    '''send_mail(
            'this is a mail from django',
            'thanking you mail',
            'jagadeeshkumar112311@gmail.com',
            ['mohankadali374@gmail.com'],
            fail_silently=False
            )'''
    if request.method == "POST":
        username=request.POST['adh']
        email=request.POST['em']
        passwd = request.POST['passwd']
        passwd2 = request.POST['passwd2']
        '''global val
        def val():
            return passwd'''
        if passwd == passwd2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('signup')
            elif(User.objects.filter(username=username).exists()):
                messages.info(request,'Adhar Exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=passwd)
                user.save();
                p=pad.objects.create(passwd=passwd,adno=username)
                p.save();

                return redirect('home')
        else:
            messages.info(request,'Password Not Same')
            return redirect('signup')
    else:
        return render(request,'signup.html')
def hospitallogin(request):
    if request.method == 'POST':
        hname=request.POST['hname']
        password=request.POST['hpasswd']
        if(len(hname)==0 or len(password)==0):
            messages.info(request,"please fill the empty feild")
            return redirect('hospitallogin')
        uname=0
        h=hospitals.objects.all()
        for i in h:
            if(i.hospital_name==hname and i.hospital_id==password):
                uname=1

        if(uname==0):
            messages.info(request,"invalid username or password")
            return redirect('hospitallogin')
        else:
            #messages.info(request,'invalid username or password')
            return redirect('pdata')
    else:
        return render(request,'hospitallogin.html')
def notlog(request):
    
    return render(request,'notlog.html')
def verify(request):
    if request.method == 'POST':
        adno=request.POST['adno']
        passwd=request.POST['passwd']
        if pad.objects.filter(adno=adno).exists():
            r=pad.objects.get(adno=adno)
            if(passwd==r.passwd):
                return redirect('upload')
            else:
                messages.info(request,'invalid password')
                return redirect('verify')
        else:
            messages.info(request,'user not exists')
            return redirect('verify')
    else:
        return render(request,'verify.html')
def patientlogin(request):
    if request.method == 'POST':
        global adn
        adn=request.POST['adno']
        passwd=request.POST['passwd']
        if pad.objects.filter(adno=adn).exists():
            r=pad.objects.get(adno=adn)
            if(passwd==r.passwd):
                return redirect('userdetails')
            else:
                messages.info(request,'invalid password')
                return redirect('signup')
        else:
            messages.info(request,'user not exists')
            return redirect('signup')
    else:
        return render(request,'patientlogin.html')
def userdetails(request):
    rep=reports.objects.filter(adno=adn)
    lst=[]
    for i in rep:
        obj=tempreports()
        obj.dat=i.dat
        obj.adno=i.adno
        obj.diag=decryption(i.diag,key=adn)
        obj.prec=decryption(i.prec,key=adn)
        obj.rem=decryption(i.rem,key=adn)
        obj.disease=decryption(i.disease,key=adn)
        obj.urlf=i.urlf
        lst.append(obj)
    return render(request,'userdetails.html',{'lst':lst})
def pdata(request):
    if request.method == 'POST':
       # print("hi")
        global adno
        adno=request.POST['adno']
        uobj=User.objects.get(username=adno)
        if len(adno)<12 or len(adno)>12:
            messages.info(request,'Enter a valid Adhaar Number')
            return redirect('pdata')
        else:
            rep=reports.objects.filter(adno=adno)
            r={'rep':rep}
            #return render(request,'pdataview.html',r)
            return redirect('pdataview')
    else:
        return render(request,'pdata.html')
def decryption(s,key):
    s=list(s)
    n=len(s)
    key=(key*n)[:n]
    for i in range(0,len(s)):
        if (s[i] in capital):
            p = ((capital.index(s[i]) - nl.index(key[i]))) % 26
            s[i] = capital[p]
        elif (s[i] in small):
            t = s.index(s[i])
            p = ((small.index(s[i]) - nl.index(key[i]))) % 26
            s[i] = small[p]
        elif(s[i] in sc):
            p = ((sc.index(s[i]) - nl.index(key[i]))) % 28
            s[i] = sc[p]
        elif(s[i] in nl):
            p = ((nl.index(s[i]) - nl.index(key[i]))) % 10
            s[i] = nl[p]
    c=("".join(s))    
    return c
def pdataview(request):
    rep=reports.objects.filter(adno=adno)
    lst=[]
    for i in rep:
        obj=tempreports()
        obj.dat=i.dat
        obj.adno=i.adno
        obj.diag=decryption(i.diag,key=adno)
        obj.prec=decryption(i.prec,key=adno)
        obj.rem=decryption(i.rem,key=adno)
        obj.disease=decryption(i.disease,key=adno)
        obj.urlf=i.urlf
        lst.append(obj)
    return render(request,'pdataview.html',{'lst':lst})
    
def cont(request):
    return render(request,'cont.html')
'''def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        passwd=request.POST['passwd']
        adno=request.POST['adno']
        user=User.objects.Create_User(username=adno,password=passwd,email=email)
        user.save();
        return redirect('home')
        
        return redirect('home')
    else:
        return render(request,'signup.html')'''

"""def logout(request):
    auth.logout(request)
    return redirect('logedin')
def sendmail(request):
    #send_mail('mail through django','hi this is an mail from sushma....... ','suahmakurella@gmail.com',['kikkisetti8bkvnad@kvsernakulamregion.in'],fail_silently=False)

    #pywhatkit.sendwhatmsg("+91 9985902617","hi",21,40)
    return render(request,'sendmail.html')"""
def encryption(s,key):
    print('hi')
    s=list(s)
    n=len(s)
    key=(key*n)[:n]
    c=''
    for i in range(0, len(s)):
        if (s[i] in capital):
            p = (capital.index(s[i]) + nl.index(key[i])) % 26
            s[i] = capital[p]
        elif (s[i] in small):
            p = ((small.index(s[i]) + nl.index(key[i]))) % 26
            s[i] = small[p]
        elif(s[i] in sc):
            p = ((sc.index(s[i]) + nl.index(key[i]))) % 28
            s[i] = sc[p]
        elif(s[i] in nl):
            p = ((nl.index(s[i]) + nl.index(key[i]))) % 10
            s[i] = nl[p]
    c=("".join(s))
    return c


def about(request):
    return render(request,'about.html')

def upload(request):
    if request.method=='POST':
        adh = request.POST['adh']
        kw=User.objects.filter(username=adh)
        k=adh
        date=request.POST['date']
        diag=encryption(request.POST['diag'],key=k)
        rem=encryption(request.POST['remarks'],key=k)
        urlf=(request.POST['urlf'])
        prec=encryption(request.POST['prec'],key=k)
        disease=encryption(request.POST['disease'],key=k)
        
        rep = reports.objects.create(dat=date,diag=diag,prec=prec,rem=rem,disease=disease,adno=adh,urlf=urlf)
        rep.save();
        return redirect('home')
    else:
        return render(request,'upload.html')