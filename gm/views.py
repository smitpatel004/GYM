from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
from django.contrib import messages
def hame(request):
    return render(request,'index.html')

def Equpment(request):
    return render(request,"equipment.html")

def chestB(request):
    return render(request,"chestbegnier.html")

def absB(request):
    return render(request,"AB.html")


def Exe(request):
    data =Exercise.objects.all()
    context ={'Exer':data}

    print(data)
    return render(request,"show2.html",context)

# def register_page(request):
#     if request.method == "POST":
         
#          username=request.POST.get('username')
#          weight=request.POST.get('weight')
#          height=request.POST.get('height')
#          gender=request.POST.get('gender')
#          name=request.POST.get('pushups')
#          request.POST.get('gender')
#          email=request.POST.grt('email')




        
#     GymUser =   GYMUSER.objects.create(
#              username=username,
#              weight=weight,
#             height=height,
#             gender=gender,
#             name=name,
#             email=email,

#         )
#     print(GymUser)
#     GymUser.save()
#     user =GYMUSER.objects.filter(username=username)
#     if user.exists():
#             print("taken already")
#             messages.info(request,'already taken')
#             return redirect('/register/')
    
#     return render(request,'register.html')


def login_page(request):
    if request.method=="POST":
        print("in login")
        username= request.POST.get('username')
        password=request.POST.get('password')
        print(username,"username")
        print(password," password")

        # if User.objects.filter(username=username).exists():
        #     print("in error")
            
        #     return redirect('/gm/login')
        user=authenticate(username=username,password=password)
        print("user",user)
        if(user is None):
            return redirect('/gm/login')
        else:
            login(request,user)
            return redirect('/gm')
    return render(request,"login.html")

def register(request):
    
    if request.method=="POST":
        
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'username already exist')
            return redirect('/gm/register')
        


        user =User.objects.create(
            first_name=first_name,
        last_name=last_name,
        username=username,
        # password=password

        )
        user.set_password(password)
        user.save()
        messages.info(request,'account create')
        return redirect('/gm/login')
    print("end")

    return render(request,"register.html")
from django.shortcuts import redirect, get_object_or_404
def logout(request):
    user = get_object_or_404(User, id=request.user.id)
    user.delete()

    


    return redirect('/gm/login')



 




# def chestA(request):
#     return render(request,"chestbegnier.html")





