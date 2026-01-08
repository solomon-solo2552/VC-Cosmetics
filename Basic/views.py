from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method=="POST":
        number1=int(request.POST.get("txt_num1"))
        number2=int(request.POST.get("txt_num2"))
        result=number1+number2
        return render(request,'Basic/Add.html',{'result':result})
    else:
        return render(request,'Basic/Add.html')

def ls(request):
    if request.method=="POST":
        number1=int(request.POST.get("txt_num1"))
        number2=int(request.POST.get("txt_num2"))
        number3=int(request.POST.get("txt_num3"))
        if number1 > number2 and number1 > number3:
          largest= number1
        elif number2 > number1 and number2 > number3:
          largest= number2
        elif number3 > number2 and number3 > number1:
          largest=number3

        if number1 < number2 and number1 < number3:
          smallest= number1
        elif number2 < number1 and number2 < number3:
          smallest= number2
        elif number3 < number2 and number3 < number1:
          smallest=number3
        return render(request,'Basic/Largestofthree.html',{'largest':largest,'smallest': smallest})
    else:
        return render(request,'Basic/Largestofthree.html')







def reg(request):
    if request.method=="POST":
        Name=request.POST.get("txt_name")
        Gender=request.POST.get("radio")
        Department=request.POST.get("sel_dept")
        Mark1=int(request.POST.get("txt_num1"))
        Mark2=int(request.POST.get("txt_num2"))
        Markr3=int(request.POST.get("txt_num3"))  
        Total=Mark1+Mark2+Markr3
        Percentage=(Total/300)*100
        if(Percentage>=90):
            Grade="A+"
        elif(Percentage>=80):
            Grade="A"
        elif(Percentage>=70):
            Grade="B+"
        elif(Percentage>=60):
            Grade="B"
        elif(Percentage>=50):
            Grade="C+"
        return render(request,'Basic/Registerlist.html',{'Name':Name,'Gender': Gender,'Department':Department,'Total': Total,'Percentage':Percentage,'Grade': Grade})
    else:
        return render(request,'Basic/Registerlist.html')

        
       

   
        

       
    