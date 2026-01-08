from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from Shop.models import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.conf import settings

# Create your views here.
def userreg(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        Name=request.POST.get('txt_name')
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_password')
        Address=request.POST.get('txt_address')
        contact=request.POST.get('txt_contact')
        Photo=request.FILES.get('file_photo')
        Place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=Name,user_email=Email,user_password=Password,user_address=Address,user_contact=contact,user_photo=Photo,place=Place)
        return redirect("Guest:userreg")
    else:
        return render(request,'Guest/UserRegistration.html',{'dis':dis})


def ajaxplace(request):
    district = tbl_district.objects.get(id=request.GET.get("did"))   
    Place = tbl_place.objects.filter(district=district)
    return render(request,"Guest/AjaxPlace.html",{"place":Place})

def login(request):
   
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_password')
        admincount=tbl_admin.objects.filter(admin_email=Email,admin_password=Password).count()
        usercount=tbl_user.objects.filter(user_email=Email,user_password=Password).count()
        shopcount=tbl_shop.objects.filter(shop_email=Email,shop_password=Password).count()
        if usercount>0:
            user=tbl_user.objects.get(user_email=Email,user_password=Password)
            request.session['uid']=user.id
            request.session['uname']=user.user_name
            return redirect('User:homepage')
        elif shopcount>0:
            shop=tbl_shop.objects.get(shop_email=Email,shop_password=Password)
            request.session['sid']=shop.id
            request.session['sname']=shop.shop_name
            return redirect('Shop:homepage')
        elif admincount>0:
            admin=tbl_admin.objects.get(admin_email=Email,admin_password=Password)
            request.session['aid']=admin.id
            request.session['aname']=admin.admin_name
            return redirect('Admin:homepage')
    else:
            return render(request,'Guest/Login.html',{'msg':'invalid login'})
    
def shopreg(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        Name=request.POST.get('txt_name')
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_password')
        Address=request.POST.get('txt_address')
        contact=request.POST.get('txt_contact')
        Logo=request.FILES.get('file_logo')
        Proof=request.FILES.get('file_proof')
        Place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_shop.objects.create(shop_name=Name,shop_email=Email,shop_password=Password,shop_address=Address,shop_contact=contact,shop_logo=Logo,shop_proof=Proof,place=Place)
        return redirect("Guest:shopreg")
    else:
        return render(request,'Guest/ShopRegistration.html',{'dis':dis})

def index(request):
    return render(request,'Guest/Index.html')



# Temporary token storage (use DB for production)
RESET_USER_TOKENS = {}

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = tbl_user.objects.get(user_email=email)
            token = get_random_string(30)
            RESET_USER_TOKENS[token] = user.id

            reset_link = request.build_absolute_uri(f"/reset-password/{token}/")
            send_mail(
                "Reset Your Password",
                f"Click here to reset your password: {reset_link}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False
            )
            return render(request, "Guest/email_sent.html", {"email": email})
        except tbl_user.DoesNotExist:
            return render(request, "Guest/forgot_password.html", {"error": "Email not found"})

    return render(request, "Guest/forgot_password.html")



def reset_password(request, token):
    user_id = RESET_USER_TOKENS.get(token)
    if not user_id:
        return render(request, "Guest/index.html")

    if request.method == "POST":
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        if password != confirm:
            return render(request, "Guest/reset_password.html", {"error": "Passwords do not match"})

        user = tbl_user.objects.get(id=user_id)
        user.user_password = password  # You should hash passwords!
        user.save()
        del RESET_USER_TOKENS[token]

        return redirect("Guest:login")  # Replace with your login URL name

    return render(request, "Guest/reset_password.html")
