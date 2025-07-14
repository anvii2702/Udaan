import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest.api import *

# Create your views here.
def index_user(request):
    json_file_path_airport = 'static/API/Flight/airport.json'
    with open(json_file_path_airport, 'r', encoding='utf-8') as json_file:
        data_airport = json.load(json_file)
    return render(request, 'frontend/index.html', context={'data_airport': data_airport})

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('sign_up')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('sign_up')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('sign_up')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('sign_in')

    return render(request, 'frontend/sign-up.html')

def sign_in(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index_user')
        else:
            error = "Invalid email or password."
            return render(request, 'frontend/sign-in.html', {'error': error})
    else:
        return render(request, 'frontend/sign-in.html')

def about_us(request):
    return render(request,'frontend/about.html')

def contact_us(request):
    return render(request,'frontend/contact.html')

def privacy_policy(request):
    return render(request,'frontend/privacy-policy.html')

def terms_and_conditions(request):
    return render(request,'frontend/terms-of-service.html')

def flight_listing(request):
    if request.method == "GET":
        try:
            max_price = 0
            
            dataGet = request.GET.get('onward')
            dataGetDict = json.loads(dataGet)
            print(dataGetDict)

            # Load airport data (unchanged)
            json_file_path_airport = 'static/API/Flight/airport.json'   
            with open(json_file_path_airport, 'r', encoding='utf-8') as json_file:
                trpj_data_airport = json.load(json_file)
            
            json_file_path_airline = 'static/API/Flight/airline.json'
            with open(json_file_path_airline, 'r', encoding='utf-8') as json_file:
                trpj_data_airline = json.load(json_file)
            
            # Load flight data from a local JSON file instead of an API
            json_file_path_flight = 'flight_search.json'
            with open(json_file_path_flight, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            # print(type(data), 'Flight data loaded from JSON')

            if not data:
                return render(request, "404.html", context={"image":"images/flights/plane.png", "heading":"No Flights Available", "url":"/", "page":"Home", "message":"No flights were found for this route and date combination. Modify your search and try again"})

            # Assuming the JSON structure contains a "TripDetails" key
            trip_details = data.get("TripDetails", [])
            search_key = data.get("Search_Key", "")
            request.session["serach_key"] = search_key
            
            if len(trip_details) == 1:
                paginator = Paginator(trip_details[0]["Flights"], 25)  
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                # print('Pagination object:', page_obj)
                context = {"data":page_obj, "data2":json.dumps(data),"parseData": dataGetDict, "airport": trpj_data_airport}
                return render(request, 'frontend/flight-list.html', context=context)
            else:
                raise ValueError("Unexpected trip details length")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, "404.html", context={"image":"images/flights/plane.png", "heading":"No Flights Available", "url":"/", "page":"Home", "message":"No flights were found for this route and date combination. Modify your search and try again"})

   

def flight_details(request,flight_key,fare_id):
    flyshop_fare_rule(request.session["serach_key"],flight_key,fare_id)
    flyshop_air_reprice(request.session["serach_key"],flight_key,fare_id,"9999999999")
    
    return render(request,'frontend/flight-detail.html')

def flight_booking(request):
    return render(request,'frontend/flight-booking.html')

def staff_dashboard(request):
    return render(request,'dashboard/admin-dashboard.html')

def my_login(request):
    return redirect('sign_in')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('my_login')
