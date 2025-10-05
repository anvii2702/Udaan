from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from datetime import datetime, timezone
from django.contrib.auth import get_user
from .utils import encode_email, generate_unique_transaction
from django.db import transaction
from django.db.models import Count,Sum,F,Case, When
from django.db.models.functions import ExtractMonth,Coalesce
# from tripnroll.phone_pay import Payment_url
from django.contrib.auth.decorators import login_required

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
            if user.is_superuser:
               print('1')
               return redirect ('superadmin_dashborad') 
            elif hasattr(user,'staff_profile'):
                print('2')
                return redirect ('staff_dashboard')
            elif hasattr(user,'customer_profile'):
                print('3')
                return redirect ('index_user')
        else:       
            error = "Invalid email or password."
            return render(request, 'frontend/sign-in.html', {'error': error})
    else:
        return render(request, 'frontend/sign-in.html')

def profile(request):
    return (request, 'frontend/profile.html')

def forgot_Password(request):    
    return render(request, 'forgot-password.html')
 
def reset_Password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        user = CustomUser.objects.filter(email=email).first()
        if password1==password2:
           user.set_password(password1)
           user.save()
           messages.success(request, 'Password reset successfully.')
           return redirect('frontend/sign_in.html')
        else:
            messages.error(request, 'Password do not match.')
            return redirect('frontend/reset_password.html')
            
    return render(request, 'frontend/reset_password.html')

def logout_view(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect ('index_user')

