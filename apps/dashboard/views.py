from django.shortcuts import render,HttpResponse,redirect
from ..dashboard.models import *
from ..login.models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
import bcrypt
def index(request):
    me = User.objects.get(id=request.session['user_id'])
    print(me)
    context={
        'my_items':me.add.all(),
        'items': Mylist.objects.all(),
        'all_items':List.objects.all()
    }
    print(me.add.all())
    return render(request,'dashboard/index.html',context)
def logout(request):
    request.session.clear()
    return redirect('/')
def remove(request):
    List.objects.remove_item(request.POST)
    return redirect(reverse('dashboard:index'))
def delete(request):
    List.objects.delete(request.POST)
    return redirect(reverse('dashboard:index'))
def add(request):
    Mylist.objects.addding(request.POST)
    return redirect(reverse('dashboard:index'))
def additem(request):
    context={
        'me':User.objects.get(id=request.session['user_id'])
    }
    return render(request,'dashboard/create.html',context)
def create(request):
    errors = List.objects.add_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        context={
        'me':User.objects.get(id=request.session['user_id'])
        }
        return render(request,'dashboard/create.html',context)
    else:
        return redirect(reverse('dashboard:index'))
def info(request,id):
    item=Mylist.objects.get(id=id)
    context={
        'item':Mylist.objects.get(id=id),
    }
    return render(request,'dashboard/info.html',context)