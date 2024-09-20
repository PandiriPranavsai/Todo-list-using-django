from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()

    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request, 'todo.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if len(password)<6:
            messages.error(request,'Password contain atleast 7 characters')
            return redirect('register')
        
        users=User.objects.filter(username=username)
        if users:
            messages.error(request,'Error,Username already exists')
            return redirect('register')
        
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()

        messages.success(request,'successfully user created login now')
        return redirect('login')
    return render(request,'register.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request,"check both the username and password and login in again")
            return redirect('login')
    return render(request,'login.html')



@login_required
def DeleteTask(request,id):
    get_todo=todo.objects.get(user=request.user,id=id)
    get_todo.delete()
    return redirect('homepage')


@login_required
def Update(request, id=id):
    get_todo = todo.objects.get(user=request.user,id=id)
    get_todo.status = True
    get_todo.save()
    return redirect('homepage')
   


def LogoutView(request):
    logout(request)
    return redirect('login')