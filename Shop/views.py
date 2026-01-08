from django.shortcuts import render,redirect
from Shop.models import *
from User.models import *
# Create your views here.
def ajaxcategory(request):
    cat=tbl_category.objects.filter(brand=request.GET.get('bid'))
    return render(request,'Shop/AjaxCategory.html',{'cat':cat})

def product(request):
    brand=tbl_brand.objects.all()
    cat=tbl_category.objects.all()
    prod=tbl_product.objects.all()
    shopid=tbl_shop.objects.get(id=request.session['sid'])
    if request.method=="POST":
        Name=request.POST.get('txt_name')
        Details=request.POST.get('txt_details')
        Price=request.POST.get('txt_price')
        Photo=request.FILES.get('file_photo')
        Category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        # Brand=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_product.objects.create(product_name=Name,product_price=Price,product_photo=Photo,product_details=Details,category=Category,shop=shopid)
        return render(request,'Shop/Product.html',{'prod':prod,'bnd':brand,'cat':cat})
    else:
        return render(request,'Shop/Product.html',{'prod':prod,'bnd':brand,'cat':cat})
    
def delproduct(request,pid):
    if 'sid' not in request.session:
        return redirect("Guest:login")
    tbl_product.objects.get(id=pid).delete()
    return redirect('Shop:product')

def addstock(request,pid):
    if 'sid' not in request.session:
        return redirect("Guest:login")
    productid=tbl_product.objects.get(id=pid)
    stocks=tbl_stock.objects.filter(product=pid)
    if request.method=="POST":
        Stock=request.POST.get('txt_stock')
        tbl_stock.objects.create(stock_quantity=Stock,product=productid)
        return render(request,'Shop/Stock.html',{'prod':stocks})
    else:
        return render(request,'Shop/Stock.html',{'prod':stocks})
    
def myprofile(request):
    shop= tbl_shop.objects.get(id=request.session['sid'])
    return render(request,'Shop/Myprofile.html',{'shop':shop})  

def logout(request):
    if 'sid' not in request.session:
        return redirect("Guest:login")
    del request.session["sid"]
    return redirect("Guest:login")

    
def editprofile(request):
    editdata= tbl_shop.objects.get(id=request.session['sid'])
    if request.method=="POST":
        editdata.shop_name=request.POST.get('txt_name')
        editdata.shop_email=request.POST.get('txt_email')
        editdata.shop_address=request.POST.get('txt_address')
        editdata.shop_contact=request.POST.get('txt_contact')
        editdata.save()
        return redirect('Shop:myprofile')
    else:
        return render(request,'Shop/Editprofile.html',{'edit':editdata})


def changepassword(request):
    data= tbl_shop.objects.get(id=request.session['sid'])
    if request.method=="POST":
     if data.shop_password==request.POST.get('txt_oldpass'):
       if request.POST.get('txt_newpass')==request.POST.get('txt_confirmpass'):
           data.shop_password=request.POST.get('txt_newpass')
           data.save()
           return render(request,'Shop/changepassword.html')
    else:
        return render(request,'Shop/changepassword.html')

def homepage(request):
    if 'sid' not in request.session:
        return redirect("Guest:login")
    name = request.session.get('sname')
    return render(request,'Shop/Homepage.html',{'name':name})

def viewbooking(request):
    if 'sid' not in request.session:
        return redirect("Guest:login")
    cart=tbl_cart.objects.filter(booking__booking_status__gte=2)
    return render(request,'Shop/ViewBooking.html',{'cart':cart})

def packed(request,bid):
    if 'sid' not in request.session:
        return redirect("Guest:login")
    bookingdata=tbl_booking.objects.get(id=bid)
    bookingdata.booking_status=3
    bookingdata.save()
    return redirect('Shop:viewbooking')

def shipped(request,sid):
    if 'sid' not in request.session:
        return redirect("Guest:login")
    bookingdata=tbl_booking.objects.get(id=sid)
    bookingdata.booking_status=4
    bookingdata.save()
    return redirect('Shop:viewbooking')

def delivered(request,did):
    if 'sid' not in request.session:
        return redirect("Guest:login")
    bookingdata=tbl_booking.objects.get(id=did)
    bookingdata.booking_status=5
    bookingdata.save()
    return redirect('Shop:viewbooking')

def complete(request,cid):
    if 'sid' not in request.session:
        return redirect("Guest:login")
    bookingdata=tbl_booking.objects.get(id=cid)
    bookingdata.booking_status=6
    bookingdata.save()
    return redirect('Shop:viewbooking')