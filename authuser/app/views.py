from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout as auth_logout
# Create your views here.


def homepage(request):
    return render(request,'home.html')

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        email_check = User.objects.filter(email=email).exists()
        if email_check ==True:
            messages.error(request,'This email is already registered')
            return redirect('signup')
        elif password != cpassword:
            messages.error(request,'password and confirm password does not match!')
            return redirect('signup')
        else:
            user_at = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
            user_at.save()
            messages.success(request,"your account successfully registered")
            return redirect('login')
    return render(request,'signup.html')



def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username = username,password=password)
       
        if user is not None:
            login(request,user)
            messages.success(request,"you've successfully login!!")
            return redirect('home')
        else:
            messages.error(request,"something went wrong")
            return redirect('login')
        
    return render(request,'login.html')

def logout_page(request):
    auth_logout(request)
    messages.success(request,"you've successfully loggedout!")
    return redirect('home')