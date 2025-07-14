from decimal import Decimal
from itertools import chain
import json
import re
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import authenticate, login, logout

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

def Signup(request):
    if request.method == "POST":
        f_name = request.POST.get('first__name')
        l_name = request.POST.get('last__name')
        mobile = request.POST.get('mobile__no')
        email = request.POST.get('registration__email')
        password1 = request.POST.get('login[password]')
        password2 = request.POST.get('password_2')
        if request.POST.get('Agent'):
            Agent_ = True
        else:
            Agent_ = False

        u = CustomUser.objects.create_user(contact_no=mobile, password=password1, email=email, first_name=f_name, last_name=l_name, is_staff=False, is_active=True, is_customer=True, is_Agent=Agent_,)
        u.save()
        ##print(type(u))
        ##print(u)
        if 'Agent' in request.POST:
            
           Agent.objects.create(user=u, is_Varified=False, PanCard='', AadharCard='', Gstno='', Address='')
          
           return redirect('/Users/login/')
        else:
            return redirect("/Users/login/")
    else:
         
        return render(request, 'signup.html')

def Forgot_Password(request):

    
    return render(request, 'forgot-password.html')

def Reset_Password(request):
    
        return render(request, 'reset-password.html')

