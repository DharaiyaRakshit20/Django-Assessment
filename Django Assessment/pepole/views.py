from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import random
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
# Create your views here.

def Register(request):
    global user_otp
    if request.method == "POST":
        if request.POST["password"] == request.POST["cpassword"]:
            user_otp=random.randint(100000,999999)
            subject = 'Bansari Luxeriya Register OTP'
            message = f'You Register Is Bansri luxariya And Your Register Success before OTP:  {user_otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST["email"], ]
            send_mail( subject, message, email_from, recipient_list )
            global temp
            temp={
                "name":request.POST["name"],
                "email":request.POST["email"],
                "password":request.POST["password"],
                "cpassword":request.POST["cpassword"]
            }
            return render(request,"otp.html")
        else:
            return render(request,"signin.html",{"msg":"Your Password and Confrom Password Is Not Match.."})
    else:
        return render(request,"signin.html")
    
def otp(request):
    if request.method == "POST":
        if user_otp ==int(request.POST["otp"]):
            register.objects.create(
                name=temp["name"],
                email=temp["email"],
                password=make_password(temp["password"]),
                cpassword=make_password(temp["cpassword"])
            )
            return render(request,"index.html")
        else:
            return render(request,"otp.html",{"msg":"Your OTO Not Match.."}) 
    else:
        return render(request,"signin.html")  

def login(request):
    if request.method == "POST":
        try:
            data=register.objects.get(email=request.POST["email"])
            if check_password(request.POST["password"],data.password):
                request.session["email"]=request.POST["email"]
                return render(request,"index.html",{"data":data})
            else:
                return render(request,"login.html",{"msg":"Your Password Not Coreecet.."})
        except:
            return render(request,"login.html",{"msg":"Your Email Is Not Valid..."})
    else:
        return render(request,"login.html")


def logout(request):
    del request.session["email"]
    return render(request,"login.html",{"msg":"You Logout Successfully.."})

def profile(request):
    user_data=register.objects.get(email=request.session["email"])
    if request.method == 'POST':
        data=register.objects.get(email=request.session["email"])
        try:
            profile_iamges=request.FILES["propic"]
        except:
            profile_iamges=data.propic
        if request.POST["newpassword"]:
            if check_password(request.POST["password"],data.password):
                if request.POST["newpassword"] == request.POST["newcpassword"]:
                    data.name=request.POST["name"]
                    data.password=make_password(request.POST["newpassword"])
                    data.cpassword=make_password(request.POST["newcpassword"])
                    data.propic=profile_iamges
                    data.save()
                    return render(request,"profile.html",{"data":data,"user_data":user_data,})
                else:
                    return render(request,"profile.html",{"data":data,"user_data":user_data,"msg":"Your New Password and Conform New passowrd Not Match.."})
            else:
                return render(request,"profile.html",{"data":data,"user_data":user_data,"msg":"Your Old Password Is Not Mtach.."})
        else:
            data.name=request.POST["name"]
            data.propic=profile_iamges
            data.address=request.POST["address"]
            data.save()
            return render(request,"profile.html",{"data":data,"user_data":user_data,"msg":"Profile Updated Successfully..."}) 
    else:
        data=register.objects.get(email=request.session["email"])
        return render(request,"profile.html",{"data":data,"user_data":user_data})  
 
def back(request):
    return render(request,"index.html")
  
def members(request):
    members=register.objects.all()
    return render(request,"society_members.html",{"members":members}) 

def details(request,pk):
    details=register.objects.get(id=pk)
    return render(request,"details.html",{"details":details})

def show_notice(request):
    all_notice=notc.objects.all()
    return render(request,"notice.html",{"all_notice":all_notice})

def create_notice(request):
    if request.method == "POST":
        name = request.POST["name"]
        notice = request.POST["Notice"]
        date_str = request.POST["datetime"]

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return render(request, "create_notice.html", {"error": "Invalid date format. Please use YYYY-MM-DD."})

        notc.objects.create(
            name=name,
            notice=notice,
            date=date
        )
        return render(request, "create_notice.html", {"msg": "Add Notice...."})
    else:
        return render(request, "create_notice.html")
    

def watchmen(request):
    watchmen_data=S_watchmen.objects.all()
    return render(request,"watchment.html",{"watchmen_data":watchmen_data,"msg":"Watchmen Deleted Successfylly.."})

def add_watchmen(request):
    if request.method == 'POST':
        S_watchmen.objects.create(
           w_propic=request.FILES["Watchmen_propic"],
           name=request.POST["name"],
           email=request.POST["email"],
           gat_no=request.POST["getno"],
           mobile=request.POST["mobile"]
        )
        return render(request,"add_watchmen.html",{"msg":"Add Watchmen.."})
    else:
        return render(request,"add_watchmen.html")
    
def Watchmen_details(request,pk):
    watchmen_data=S_watchmen.objects.get(id=pk)
    return render(request,"watchmen_detail.html",{"watchmen_data":watchmen_data})

def delete(request,pk):
    watchmen_delete=S_watchmen.objects.get(id=pk)
    watchmen_delete.delete()
    # watchmen_delete.save()
    return watchmen(request)

def event(request):
    all_event=Event.objects.all()
    return render(request,"all_event.html",{"all_event":all_event,"msg":"Add Event..."})

def add_event(request):
    if request.method == 'POST':
        Event.objects.create(
            E_images=request.FILES["Event_Propic"],
            E_name=request.POST["E_Name"],
            E_date=request.POST["E_Date"],
            E_time=request.POST["E_Time"],
            E_releted=request.POST["E_Releted"]
        )
        return event(request)
    else: 
        return render(request,"add_event.html")
    
def Event_details(request,pk):
    E_details=Event.objects.get(id=pk)
    return render(request,"event_detail.html",{"E_details":E_details})