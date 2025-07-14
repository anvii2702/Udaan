import json
import requests
from flights_tickets.settings import trpj_api_url,trpj_apikey,flyshop_api_url,flyshop_password,flyshop_userid,flyshop_IP
from django.core.cache import cache
import hashlib
json_file_path = 'static/API/Flight/India_cities.json'
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    trpj_cities_global = json.load(json_file)
    
    
json_file_path_airport = 'static/API/Flight/airport.json'

with open(json_file_path_airport, 'r', encoding='utf-8') as json_file:
        trpj_data_airport = json.load(json_file)

json_file_path_airline = 'static/API/Flight/airline.json'

with open(json_file_path_airline, 'r', encoding='utf-8') as json_file:
        trpj_data_airline = json.load(json_file)

# def trpj_flight_search(data):
#     data_hash = hashlib.md5(str(data).encode()).hexdigest()
#     CACHE_KEY = f"flight_search_{data_hash}"
            
#     search_request = cache.get(CACHE_KEY)
#     if not search_request:
#         headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
        
#         def doSearch(base_url, apikey, endpoint, search_request):
#             print("searching Flight list...")
#             url = base_url + endpoint
#             print("Request URL:", url)
    
#             try:
#                 response = requests.post(url, data=json.dumps(search_request),
#                                           headers=headers)
#                 print("after dumps ", search_request)
#                 print("Response Status Code:", response.status_code)
#                 if response.ok:
#                     response_content = response.content.decode('utf-8')  # Decode response content
#                     response_data = json.loads(response_content)   
#                     cache.set(CACHE_KEY, response_data, timeout=60*15)
#                     return response_data 
#                 else:
#                     print("Error Response:", response.text, response)
#             except Exception as e:
#                 print("Error:", str(e))
#                 return ("Error:", str(e))
        
#         response = doSearch(trpj_api_url, trpj_apikey, '/fms/v1/air-search-all', data)
#         return response
#     else:
#         # If data is found in cache, return it directly
#         return search_request


# def trpj_flight_oneway_review(price_id):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 # with open("flightobj.json", "w") as outfile:
#                 #     json.dump(response.json(), outfile)
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request = {
     
#             "priceIds" : [price_id]
#     }
#     print(search_request)
#     return doSearch(trpj_api_url, trpj_apikey, '/fms/v1/review',
#     search_request)

# def trpj_flight_return_review(price_id,price_id1):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 # with open("flightobj.json", "w") as outfile:
#                 #     json.dump(response.json(), outfile)
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request = {
     
#             "priceIds" : [price_id,price_id1]
#     }
#     print(search_request)
#     return doSearch(trpj_api_url, trpj_apikey, '/fms/v1/review',
#     search_request)

# def trpj_flight_return_review_multicity(price_id):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 # with open("flightobj.json", "w") as outfile:
#                 #     json.dump(response.json(), outfile)
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request = {
     
#             "priceIds" : price_id
#     }
#     print(search_request)
#     return doSearch(trpj_api_url, trpj_apikey, '/fms/v1/review',
#     search_request)



# def trpj_fare_rule_api(price_id):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 # with open("flightrule.json", "w") as outfile:
#                 #     json.dump(response.json(), outfile)
                    
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request = {
     
#         "id": price_id,
#         "flowType": "REVIEW"
#     }
#     print(search_request)
#     return doSearch(trpj_api_url, trpj_apikey, '/fms/v2/farerule',
#     search_request)



# def trpj_seat_map(booking_id):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 # with open("flighseat.json", "w") as outfile:
#                 #     json.dump(response.json(), outfile)
                    
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request = {
    
#     "bookingId": booking_id
    
#     }
#     print(search_request)
#     return doSearch(trpj_api_url, trpj_apikey, '/fms/v1/seat',
#     search_request)



# def trpj_intsant_flight_booking(booking_id,amount,travellerInfo,gstInfo,contact_info,deliveryInfo):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 # with open("flighseat.json", "w") as outfile:
#                 #     json.dump(response.json(), outfile)
                    
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request ={
#     "bookingId": booking_id,
#     "paymentInfos": [
#       {
#         "amount": float(amount) 
#       }
#     ],
#     "travellerInfo": travellerInfo,
   
#     "deliveryInfo": deliveryInfo
# }   
#     if contact_info != {}:
#         search_request["contactInfo"]=contact_info
#     if gstInfo != {}:
#      search_request["gstInfo"]= gstInfo,
#     print(search_request,"ayein")
#     return doSearch(trpj_api_url, trpj_apikey, '/oms/v1/air/book',
#     search_request)



# def trpj_flight_booking_hold(booking_id,amount,travellerInfo,gstInfo,contact_info,deliveryInfo):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 # with open("flighseat.json", "w") as outfile:
#                 #     json.dump(response.json(), outfile)
                    
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request ={
#     "bookingId": booking_id,
#     "travellerInfo": travellerInfo,
   
#     "deliveryInfo": deliveryInfo
# }   
#     if contact_info != {}:
#         search_request["contactInfo"]=contact_info
#     if gstInfo != {}:
#      search_request["gstInfo"]= gstInfo,
#     print(search_request,"ayein")
#     return doSearch(trpj_api_url, trpj_apikey, '/oms/v1/air/book',
#     search_request)



# def trpj_flight_booking_detail(booking_id):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 with open("updated_details.json", "w") as outfile:
#                     json.dump(response.json(), outfile)
                    
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request ={
#     "bookingId": booking_id
#     }
    
#     print(search_request)
#     return doSearch(trpj_api_url, trpj_apikey, "/oms/v1/booking-details",search_request)



# def trpj_confirm_flight_booking_(booking_id,amount):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 # with open("updated_details.json", "w") as outfile:
#                 #     json.dump(response.json(), outfile)
                    
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request ={
#      "bookingId": booking_id,
#      "paymentInfos": [
#        {
#          "amount": float(amount) 
#        }
#      ]
#     }
#     print(search_request)
#     return doSearch(trpj_api_url, trpj_apikey, "/oms/v1/air/confirm-book",search_request)



# def trpj_unhold_flight_booking_(booking_id,pnr):
    

#     headers = {"apikey": trpj_apikey, "Content-Type": "application/json"}
#     def doSearch(base_url, apikey, endpoint, search_request):
#         print("searching Flight list...")
#         url = base_url + endpoint
#         print("Request URL:", url)

#         try:
#             response = requests.post(url, data=json.dumps(search_request),
#             headers=headers)
#             print("Response Status Code:", response.status_code)
#             if response.ok:
#                 # with open("updated_details.json", "w") as outfile:
#                 #     json.dump(response.json(), outfile)
                    
#                 return(response.json())
#             else:
#                 print("Error Response:", response.text)
#         except Exception as e:
#             print("Error:", str(e))
#             return("Error:", str(e))
            

#     search_request ={
#     "bookingId":booking_id,
#      "pnrs":pnr
#     }
#     print(search_request)
#     return doSearch(trpj_api_url, trpj_apikey, "/oms/v1/air/unhold",search_request)


def flyshop_flight_search(data):
    data_hash = hashlib.md5(str(data).encode()).hexdigest()
    CACHE_KEY = f"flight_search_{data_hash}"
            
    search_request = cache.get(CACHE_KEY)
    if not search_request:
        headers = {'Content-Type': 'application/json'}

        
        def doSearch(base_url, userid, password,endpoint, search_request):
            print("searching Flight list...")
            url = base_url + endpoint
            print("Request URL:", url)
    
            try:
                request_data = {"Auth_Header": {
                                    "UserId":userid,
                                    "Password": password,
                                    "IP_Address": flyshop_IP,
                                    "Request_Id": "22222242423",
                                    "IMEI_Number": "45684686"
                                }}
                request_data.update(search_request)
                response = requests.post(url, data=json.dumps(request_data),headers=headers)
                print("after dumps ", url,headers,json.dumps(request_data))
                print("Response Status Code:", response.status_code)
                if response.ok:
                    response_content = response.content.decode('utf-8')  # Decode response content
                    response_data = json.loads(response_content)   
                    # print(response_data['Response_Header'])
                    if response_data['Response_Header']['Error_Code'] == "0000" and  response_data['Response_Header']['Error_Desc']=="SUCCESS" :
                        cache.set(CACHE_KEY, response_data , timeout=60*15)
                        return response_data
                    else:
                        print("Error Response:", response.text, response)
                else:
                    print("Error Response:", response.text, response)
                    return False
            except Exception as e:
                print("Error:", str(e))
                return ("Error:", str(e))
        
        response = doSearch(flyshop_api_url,flyshop_userid, flyshop_password, '/AirlineHost/AirAPIService.svc/JSONService/Air_Search', data)
        return response
    else:
        # If data is found in cache, return it directly
        return search_request


def flyshop_fare_rule(search_key,flight_key,fare_id):
    headers = {'Content-Type': 'application/json'}

    
    def doSearch(base_url, userid, password,endpoint, search_key,flight_key,fare_id):
        print("searching Flight list...")
        url = base_url + endpoint
        print("Request URL:", url)

        try:
            request_data = {"Auth_Header": {
                                "UserId":userid,
                                "Password": password,
                                "IP_Address": flyshop_IP,
                                "Request_Id": "5500887959052",
                                "IMEI_Number": "45684686"
                            }}
            request_data["Search_Key"] = search_key
            request_data["Flight_Key"] = flight_key
            request_data["Fare_Id"] = fare_id
            
            response = requests.post(url, data=json.dumps(request_data),headers=headers)
            print("after dumps ", url,headers,json.dumps(request_data))
            print("Response Status Code:", response.status_code)
            if response.ok:
                response_content = response.content.decode('utf-8')  # Decode response content
                response_data = json.loads(response_content)   
                print(response_data)
                if response_data['Response_Header']['Error_Code'] == "0000" and  response_data['Response_Header']['Error_Desc']=="SUCCESS" :
                    return response_data
                else:
                    print("Error Response:", response.text, response)
            else:
                print("Error Response:", response.text, response)
                return False
        except Exception as e:
            print("Error:", str(e))
            return ("Error:", str(e))
    
    response = doSearch(flyshop_api_url,flyshop_userid, flyshop_password, '/AirlineHost/AirAPIService.svc/JSONService/Air_FareRule', search_key,flight_key,fare_id)
    return response

def flyshop_air_reprice(search_key,flight_key,fare_id,mobile):
    headers = {'Content-Type': 'application/json'}

    
    def doSearch(base_url, userid, password,endpoint, search_key,flight_key,fare_id,mobile):
        print("searching Flight list...")
        url = base_url + endpoint
        print("Request URL:", url)

        try:
            request_data = {"Auth_Header": {
                                "UserId":userid,
                                "Password": password,
                                "IP_Address": flyshop_IP,
                                "Request_Id": "5500887959052",
                                "IMEI_Number": "45684686"
                            }}
            request_data["Search_Key"] = search_key
            request_data["AirRepriceRequests"] = [{"Flight_Key":flight_key,"Fare_Id":fare_id}]
            request_data["Customer_Mobile"] = mobile
            request_data["GST_Input"] = False
            request_data["SinglePricing"] = True
            
            
            response = requests.post(url, data=json.dumps(request_data),headers=headers)
            print("after dumps ", url,headers,json.dumps(request_data))
            print("Response Status Code:", response.status_code)
            if response.ok:
                response_content = response.content.decode('utf-8')  # Decode response content
                response_data = json.loads(response_content)   
                print(response_data)
                if response_data['Response_Header']['Error_Code'] == "0000" and  response_data['Response_Header']['Error_Desc']=="SUCCESS" :
                    return response_data
                else:
                    print("Error Response:", response.text, response)
            else:
                print("Error Response:", response.text, response)
                return False
        except Exception as e:
            print("Error:", str(e))
            return ("Error:", str(e))
    
    response = doSearch(flyshop_api_url,flyshop_userid, flyshop_password, '/AirlineHost/AirAPIService.svc/JSONService/Air_Reprice', search_key,flight_key,fare_id,mobile)
    return response
