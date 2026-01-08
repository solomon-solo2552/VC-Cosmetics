from django.http import JsonResponse
from django.shortcuts import render,redirect
from Guest.models import *
from Shop.models import *
from User.models import *
from django.db.models import Sum
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def myprofile(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    user= tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/Myprofile.html',{'user':user})    

def logout(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    del request.session["uid"]
    return redirect("Guest:login")


def editprofile(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    editdata= tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        editdata.user_name=request.POST.get('txt_name')
        editdata.user_email=request.POST.get('txt_email')
        editdata.user_address=request.POST.get('txt_address')
        editdata.user_contact=request.POST.get('txt_contact')
        editdata.save()
        return redirect('User:myprofile')
    else:
        return render(request,'User/Editprofile.html',{'edit':editdata})


def changepassword(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    data= tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
     if data.user_password==request.POST.get('txt_oldpass'):
       if request.POST.get('txt_newpass')==request.POST.get('txt_confirmpass'):
           data.user_password=request.POST.get('txt_newpass')
           data.save()
           return render(request,'User/changepassword.html')
    else:
        return render(request,'User/changepassword.html')

     
       

def homepage(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    name = request.session.get('uname')
    return render(request,'User/Homepage.html', {'name':name})  


def complaints(request,pid):
    if "uid" in request.session:
        User=tbl_user.objects.get(id=request.session["uid"])
        Product=tbl_product.objects.get(id=pid)
        complaints=tbl_complaint.objects.filter(user=User)
        if request.method=="POST":
           Content=request.POST.get('txt_content')
           
           tbl_complaint.objects.create(complaint_content=Content,user=User,product=Product)
           return redirect('User:complaint',pid)
        else:
            return render(request,'User/Complaints.html',{'complaints':complaints})
    else:
        return redirect("Guest:Login")
    
def delcomplaint(request,did):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    tbl_complaint.objects.get(id=did).delete()
    return redirect('User:MyBooking')

def MyComplaint(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    User=tbl_user.objects.get(id=request.session["uid"])
    complaints=tbl_complaint.objects.filter(user=User)
    return render(request,'User/MyComplaints.html',{'complaints':complaints})


def delcomplaint1(request,did):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    tbl_complaint.objects.get(id=did).delete()
    return redirect('User:MyComplaint')


    
def feedback(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    feedback=tbl_feedback.objects.all()
    if request.method=="POST":
        Content=request.POST.get('txt_content')
        tbl_feedback.objects.create(feedback_content=Content)
        return render(request,'User/Feedback.html',{'feedback':feedback})
    else:
        return render(request,'User/Feedback.html',{'feedback':feedback})

def viewproduct(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    category=tbl_category.objects.all()
    brand=tbl_brand.objects.all()
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    product=tbl_product.objects.all()
    for i in product:
        total_stock = tbl_stock.objects.filter(product=i.id).aggregate(total=Sum('stock_quantity'))['total']
        total_cart = tbl_cart.objects.filter(product=i.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
        print(total_stock)
        print(total_cart)
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        total =  total_stock - total_cart
        i.total_stock = total
        tot=0
        ratecount=tbl_rating.objects.filter(product=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(product=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
            # print(parry)
    datas=zip(product,parry)
    return render(request,'User/ViewProduct.html',{'product':datas,"ar":ar,'category':category,'brand':brand})

# def ajaxsearch(request):
#     cid=tbl_category.objects.get(id=request.GET.get('cid'))
#     bid=tbl_brand.objects.get(id=request.GET.get('bid'))
#     product=tbl_product.objects.filter(category=cid,brand=bid)
   
#     return render(request,'User/AjaxSearch.html',{'product':product})

# def ajaxsearch(request):
#     name = request.GET.get('name', '').strip()
#     if name:
#         product = tbl_product.objects.filter(name__icontains=name)
#     else:
#         product = tbl_product.objects.all()

#     return render(request, 'User/AjaxSearch.html', {'product': product})

# def ajaxsearch(request):
#     name = request.GET.get('name', '').strip()
#     cid = request.GET.get('cid')
#     bid = request.GET.get('bid')

#     filters = {}

#     if cid:
#         try:
#             filters['category'] = tbl_category.objects.get(id=cid)
#         except tbl_category.DoesNotExist:
#             pass

#     if bid:
#         try:
#             filters['brand'] = tbl_brand.objects.get(id=bid)
#         except tbl_brand.DoesNotExist:
#             pass

#     # Start with filtered products (if category/brand provided)
#     product_qs = tbl_product.objects.filter(**filters) if filters else tbl_product.objects.all()

#     # Further filter by name if provided
#     if name:
#         product_qs = product_qs.filter(name__icontains=name)

#     return render(request, 'User/AjaxSearch.html', {'product': product_qs})

# def ajaxsearch(request):
#     name = request.GET.get('name', '').strip()
#     print("Search query received:", name)  # Check this in Django console

#     if name:
#         product = tbl_product.objects.filter(name__icontains=name)
#     else:
#         product = tbl_product.objects.all()

#     return render(request, 'User/AjaxSearch.html', {'product': product})

from django.db.models import Sum, Avg, Value
from django.db.models.functions import Coalesce

def ajaxsearch(request):
    name = request.GET.get('name', '').strip()
    cid = request.GET.get('cid')
    bid = request.GET.get('bid')

    filters = {}
    
    if cid:
        filters['category_id'] = cid  # More efficient than get()
    
    if bid:
        filters['category__brand_id'] = bid
    
    # Get base queryset with annotations
    products = tbl_product.objects.filter(**filters) if filters else tbl_product.objects.all()
    
    # Annotate with stock and rating
    products = products.annotate(
        total_stock=Coalesce(
            Sum('tbl_stock__stock_quantity'), 
            Value(0)
        ),
        avg_rating=Coalesce(
            Avg('tbl_review__rating'), 
            Value(0)
        )
    ).select_related('category', 'shop', 'category__brand')
    
    if name:
        products = products.filter(product_name__icontains=name)
    
    return render(request, 'User/AjaxSearch.html', {
        'product': [(p, round(p.avg_rating)) for p in products],
        'ar': range(1, 6)
    })

def Addcart(request,pid):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    productdata=tbl_product.objects.get(id=pid)
    Userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user=Userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user=Userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"User/ViewProduct.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            msg="Added To cart"
            return render(request,"User/ViewProduct.html",{'msg':msg})
    else:
        bookingdata = tbl_booking.objects.create(user=Userdata)
        tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
        msg="Added To cart"
        return render(request,"User/ViewProduct.html",{'msg':msg})
    

def Mycart(request):
        if 'uid' not in request.session:
            return redirect("Guest:login")
        if request.method=="POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.booking_amount=request.POST.get("carttotalamt")
            bookingdata.booking_status=1
            bookingdata.save()
            cart = tbl_cart.objects.filter(booking=bookingdata)
            for i in cart:
                i.cart_status = 1
                i.save()
            return redirect("User:productpayment")
        else:
            bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
            if bookcount > 0:
                book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
                request.session["bookingid"] = book.id
                cart = tbl_cart.objects.filter(booking=book)
                for i in cart:
                    total_stock = tbl_stock.objects.filter(product=i.product_id).aggregate(total=Sum('stock_quantity'))['total']
                    total_cart = tbl_cart.objects.filter(product=i.product_id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
                    # print(total_stock)
                    # print(total_cart)
                    if total_stock is None:
                        total_stock = 0
                    if total_cart is None:
                        total_cart = 0
                    total =  total_stock - total_cart
                    i.total_stock = total
                return render(request,"User/MyCart.html",{'cartdata':cart})
            else:
                return render(request,"User/MyCart.html")
  
        

def DelCart(request,did):
   if 'uid' not in request.session:
        return redirect("Guest:login")
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:Mycart")

def CartQty(request):
   if 'uid' not in request.session:
        return redirect("Guest:login")
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("User:Mycart")   

def productpayment(request):
        if 'uid' not in request.session:
            return redirect("Guest:login")
   
        bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
        amt = bookingdata.booking_amount
        if request.method == "POST":
            bookingdata.booking_status = 2
            bookingdata.save()
            return redirect("User:loader")
        else:
            return render(request,"User/Payment.html",{"total":amt})
    
def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def MyBooking(request):
    User=tbl_user.objects.get(id=request.session["uid"])

    if "uid" in request.session:
        cart=tbl_cart.objects.filter(booking__user=User,booking__booking_status__gte=2)

        return render(request,'User/MyBooking.html',{'cart':cart})
    else:
        return redirect("Guest:Login")
    


def rating(request,mid):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(product=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(product=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    userid=tbl_user.objects.get(id=request.session['uid'])
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=userid,user_review=user_review,rating_data=rating_data,product=tbl_product.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(product=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(product=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(product=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)



def search_products(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    query = request.GET.get('search', '')
    if query:
        products = tbl_product.objects.filter(product_name__icontains=query) | tbl_product.objects.filter(description__icontains=query)
    else:
        products = tbl_product.objects.all()

    # If it's an AJAX request, return JSON response
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = list(products.values('product_name', 'description', 'price'))
        return JsonResponse({'products': data})
    
    return render(request, 'search.html', {'products': products, 'query': query})

def ajaxcategory(request):
    cat=tbl_category.objects.filter(brand=request.GET.get('bid'))
    return render(request,'User/AjaxCategory.html',{'cat':cat})

def ajaxsearch(request):
    data=request.GET.get('cid')
    name=request.GET.get('name')
    if data:
        product=tbl_product.objects.filter(category=data)
    if name:
        product=tbl_product.objects.filter(Q(product_name__istartswith=name) | Q(category__category_name__istartswith=name) )
        # product=tbl_product.objects.filter(category__category_name__istartswith=name)
    return render(request,'User/AjaxSearch.html',{'product':product})

def cancel(request,cid):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    booking=tbl_booking.objects.get(id=cid)
    booking.booking_status=6
    booking.save()
    return render(request,'User/Mybooking.html',{'msg':"Booking Cancelled"})