from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
import bcrypt
def index(request):
    return render(request,'login/index.html')
def create(request):
    errors = User.objects.basic_validator(request.POST) 
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:   
        user= User.objects.get(email=request.POST['email']).id
        username = User.objects.get(id=user).first_name
        request.session['user_id']=user
        request.session['username']=username
        return redirect(reverse('dashboard:index'))
def login(request):
    errors= User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        print('got')
        user= User.objects.get(email=request.POST['email']).id
        username = User.objects.get(id=user).first_name
        request.session['user_id']=user
        request.session['username']=username
        print(request.session['username'])
        return redirect(reverse('dashboard:index'))