from django.shortcuts import render,redirect,get_object_or_404
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


# def workout_view(request, workout_type):
#     # You can add logic to dynamically select a template or content based on the workout_type
#     template_name = f"{workout_type}.html"  # e.g., chestbegnier.html, legs.html, etc.
    
#     # context = {
#     #     'workout_type': workout_type,
#     #     # You can pass additional context if needed
#     # }
    
#     return render(request, template_name)


# def workout_view(request, workout_name):
#     print("start")
#     print(workout_name)
#     # Get the workout data from the database using the name in the URL
#     work=Workout.objects.all()

#     print(work)
#     workout = get_object_or_404(Workout, name=workout_name)
#     print(workout)
    
#     context = {
#         'workout': workout,  # Pass the workout data to the template
#     }
    
#     return render(request, 'workout_detail.html', context)


def workout_view(request, workout_name):
    # Fetch the workout based on the name
    workout = get_object_or_404(Workout, name=workout_name)
    print(workout,'________________________________________________')
    
    # Get all exercises related to this workout
    exercises = workout.exercises_set.all()  # Using the related_name defined in the Exercise model

    context = {
        'workout': workout,        # Pass the workout details
        'exercises': exercises,    # Pass the exercises related to this workout
    }

    return render(request, 'workout_detail.html', context)




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





