from django.shortcuts import render
from django.contrib.auth.models import auth,User
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Pst
from django.utils import timezone
import datetime

def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('home')
        else:
            return HttpResponseRedirect('signin')
    else:
        return render(request,'blog/signin.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 != password2:
            messages.info(request,'Password mismatch!')
            return HttpResponseRedirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username taken!')
            return HttpResponseRedirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return HttpResponseRedirect('register')
        else:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            auth.login(request,user)
            return HttpResponseRedirect('home')
    else:
        return render(request,'blog/register.html')

def profileview(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        print(user)
        print(request.POST)
        if 'biotext' in request.POST: 
            user.profile.bio = request.POST['biotext']
            user.save()
        else:    
            user.profile.bg_pic=request.POST['file2']
            user.save()       
        return HttpResponseRedirect('profileview')
    else:
        psts=Pst.objects.all()
        return render(request,'blog/profileview.html',{'psts':psts})

def pst(request):
    pst_text=request.POST['posttext']
    pst = Pst(pst_text=pst_text,dop=datetime.datetime.now())
    pst.save()
    psts=Pst.objects.all()
    return HttpResponseRedirect('profileview')

def signout(request):
    auth.logout(request)
    return HttpResponseRedirect('signin')

def home(request):
    return render(request,'blog/home.html')

def profile(request):
    return render(request,'blog/profile.html')