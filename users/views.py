from decimal import Decimal
from itertools import chain
import json
import re
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, JsonResponse
from datetime import datetime, timezone
from django.contrib.auth import get_user
from .utils import encode_email, generate_unique_transaction
from django.db import transaction
from django.db.models import Count,Sum,F,Case, When
from django.db.models.functions import ExtractMonth,Coalesce
# from tripnroll.phone_pay import Payment_url
from django.contrib.auth.decorators import login_required



def Login__(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('login[password]')

        #print(email, password)
        user = authenticate(email=email, password=password)
        #print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Invalid Credentials")

    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('/')


            
    #        Agent.objects.create(user=u, is_Varified=False, PanCard='', AadharCard='', Gstno='', Address='')
          
    #        return redirect('/Users/login/')
    #     else:
    #         return redirect("/Users/login/")
    # else:
         
    #     return render(request, 'signup.html')
def Sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('sign_up')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('sign_up')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('sign_up')

        user = CustomUser.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('sign_in')

    return render(request, 'frontend/sign-up.html')


def Sign_in(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index_user')
        else:
            error = "Invalid email or password."
            return render(request, 'frontend/sign-in.html', {'error': error})
    else:
        return render(request, 'frontend/sign-in.html')


def Forgot_Password(request):

    
    return render(request, 'forgot-password.html')

def Reset_Password(request):
    
        return render(request, 'reset-password.html')

