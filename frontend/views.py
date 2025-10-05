import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

# Create your views here.
User=get_user_model()
def index_user(request):
    json_file_path_airport = 'static/API/Flight/airport.json'
    with open(json_file_path_airport, 'r', encoding='utf-8') as json_file:
        data_airport = json.load(json_file)
    return render(request, 'frontend/index.html', context={'data_airport': data_airport})


def superadmin(request):
    return render(request,'dashboard/superadmin-dashboard.html')


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
            dataGet = request.GET.get('tripInfo')
            print(dataGet,"1")
            dataGetDict = json.loads(dataGet)
            print(dataGet,"2")
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

            if not dataGet:
                print("hello")
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


