from django.http import HttpResponse , FileResponse , JsonResponse
from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages , auth
import plotly
import plotly.express as px
import json
import matplotlib.pyplot as plt
from django_pandas.io import read_frame
import plotly.graph_objs as go
from myapp.models import CartItem
from django.contrib.auth.models import User , auth

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']
        
        if psw == psw_repeat:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('register')
            elif User.objects.filter(email= email).exists():
                messages.info(request, 'email is already taken')
                return redirect('register')


            else:
                user = User.objects.create_user(username= username , password= psw , email=email )
                user.save()
                messages.info(request, 'User Saved')
        else:
            messages.info(request, 'passwords not matching...')

        return redirect('/')
    else:
        return render(request , 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username , password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('map')
        else:
            messages.info(request , 'invalid username or password')
            return redirect('/')
        
        return request('login')
    else:
        return render(request , 'accounts/login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')
        
        
    
