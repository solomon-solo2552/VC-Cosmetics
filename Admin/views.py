from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Shop.models import *
from User.models import *
from django.http import JsonResponse
# Create your views here.


def homepage(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    shop=tbl_shop.objects.filter(shop_status=1)
    user=tbl_user.objects.all()
    name = request.session.get('aname')
    return render(request,'Admin/Homepage.html',{'name':name,'shop':shop,'user':user})

def logout(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    del request.session["aid"]
    return redirect("Guest:login")

def district(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    dist=tbl_district.objects.all()
    if request.method=="POST":
        District=request.POST.get('txt_dis')
        tbl_district.objects.create(district_name=District)
        return render(request,'Admin/District.html',{'dist':dist})
    else:
        return render(request,'Admin/District.html',{'dist':dist})

def deldistrict(request,did):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:district')

def editdistrict(request,eid):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get('txt_dis')
        editdata.save()
        return redirect('Admin:district')
    else:
        return render(request,'Admin/District.html',{'edit':editdata})

        
def adminreg(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    if request.method=="POST":
        Name=request.POST.get('txt_name')
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_pass')
        tbl_admin.objects.create(admin_name=Name,admin_email=Email,admin_password=Password)
        return render(request,'Admin/AdminRegistration.html')
    else:
        return render(request,'Admin/AdminRegistration.html')

def category(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    brand=tbl_brand.objects.all()
    cat=tbl_category.objects.all()
    if request.method=="POST":
        Category=request.POST.get('txt_category')
        tbl_category.objects.create(category_name=Category,brand=tbl_brand.objects.get(id=request.POST.get('sel_brand')))
        return redirect('Admin:category')
    else:
        return render(request,'Admin/Category.html',{'cat':cat,'brand':brand})


def delcategory(request,cid):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_category.objects.get(id=cid).delete()
    return redirect('Admin:category')

def editcategory(request,eid):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    editdata= tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editdata.category_name=request.POST.get('txt_category')
        editdata.save()
        return redirect('Admin:category')
    else:
        return render(request,'Admin/Category.html',{'edit':editdata})

def place(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    dis=tbl_district.objects.all()
    plc=tbl_place.objects.all()
    if request.method=="POST":
        place=request.POST.get('txt_place')
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=place,district=district)
        return render(request,'Admin/Place.html',{'dis':dis,'plc':plc})
    else:
        return render(request,'Admin/Place.html',{'dis':dis,'plc':plc})

def delplace(request,did):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_place.objects.get(id=did).delete()
    return redirect('Admin:place')

def editplace(request,eid):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    dis=tbl_district.objects.all()
    editdata= tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.place_name=request.POST.get('txt_place')
        editdata.save()
        return redirect('Admin:place')
    else:
        return render(request,'Admin/Place.html',{'edit':editdata,'dis':dis})

        
def subcategory(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    cate=tbl_category.objects.all()
    subcat=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcategory=request.POST.get('txt_subcategory')
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(subcategory_name=subcategory,category=category)
        return render(request,'Admin/Subcategory.html',{'cate':cate,'subcat':subcat})
    else:
        return render(request,'Admin/Subcategory.html',{'cate':cate,'subcat':subcat})

def delsubcategory(request,did):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_subcategory.objects.get(id=did).delete()
    return redirect('Admin:subcategory')

def editsubcategory(request,eid):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    cate=tbl_category.objects.all()
    editdata= tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        editdata.subcategory_name=request.POST.get('txt_subcategory')
        editdata.category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        editdata.save()
        return redirect('Admin:subcategory')
    else:
        return render(request,'Admin/Subcategory.html',{'edit':editdata,'cate':cate})
    

def brand(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    brand=tbl_brand.objects.all()
    category=tbl_category.objects.all()
    if request.method=="POST":

        Brand=request.POST.get('txt_brand')
       
        tbl_brand.objects.create(brand_name=Brand)
        return render(request,'Admin/Brand.html',{'brand':brand,'category':category})
    else:
        return render(request,'Admin/Brand.html',{'brand':brand,'category':category})


def delbrand(request,bid):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_brand.objects.get(id=bid).delete()
    return redirect('Admin:brand')

def editbrand(request,eid):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    editdata= tbl_brand.objects.get(id=eid)
    if request.method=="POST":
        editdata.brand_name=request.POST.get('txt_brand')
        editdata.save()
        return redirect('Admin:brand')
    else:
        return render(request,'Admin/Brand.html',{'edit':editdata})



def newshop(request):
    if "aid" in request.session:
        shopn=tbl_shop.objects.filter(shop_status=0)
        shopa=tbl_shop.objects.filter(shop_status=1)
        shopr=tbl_shop.objects.filter(shop_status=2)
        return render(request,'Admin/NewShop.html',{'shopn':shopn,'shopa':shopa,'shopr':shopr})
    else:
        return redirect("Guest:Login",{'newshop':newshop})


def verifyshop(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    shop=tbl_shop.objects.get(id=id)
    shop.shop_status=1
    shop.save()
    return redirect("Admin:newshop")


def unverifyshop(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    shop=tbl_shop.objects.get(id=id)
    shop.shop_status=2
    shop.save()
    return redirect("Admin:newshop")

def acceptedshop(request):
    
    if "aid" in request.session:
        shop=tbl_shop.objects.filter(shop_status=1)
        return render(request,'Admin/NewShop.html',{'shop':shop})
    else:
        return redirect("Guest:Login")


def rejectedshop(request):
    if "aid" in request.session:
        shop=tbl_shop.objects.filter(shop_status=2)
        return render(request,'Admin/NewShop.html',{'shop':shop})
    else:
        return redirect("Guest:Login")


def ViewComplaints(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    complaints=tbl_complaint.objects.all()
    return render(request,'Admin/ViewComplaints.html',{'comp':complaints})

def reply(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    complaint=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        complaint.complaint_reply=request.POST.get('txt_reply')
        complaint.save()
        return redirect('Admin:ViewComplaints')
    else:
        return render(request,'Admin/ReplyComplaint.html',{'comp':complaint})

def RepliedComplaints(request):
    if "aid" in request.session:
        user=tbl_user.objects.all()
        userdata=tbl_complaint.objects.filter(user_id__in=user,complaint_status=1)
        return render(request,'Admin/RepliedComplaints.html',{'userdata':userdata})
    else:
        return redirect("Guest:Login")

def admindetails(request):
    data=tbl_admin.objects.get(id=request.session['aid'])
    name = {
        "admin_name":data.admin_name
    }
    return JsonResponse({"name":name})