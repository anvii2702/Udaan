from django import template
from datetime import datetime
import json
import locale
from django.shortcuts import *

register = template.Library()

def floatcomma_indian(value):
    """
    Convert a float to a string containing Indian-style currency formatting with commas and 2 decimal places, without the currency symbol.
    """
    orig_value = value
    # print(orig_value)
    if value is not None:
        value = float(value)
        formatted_value = '{:,.2f}'.format(value)  # Format the float value with 2 decimal places and commas
        return formatted_value

    return orig_value

@register.filter(name='floatcomma_indian')
def floatcomma_indian_filter(value):
    return floatcomma_indian(value)

@register.filter(name='floatcomma_indian')
def floatcomma_indian_filter(value):
    return floatcomma_indian(value)

@register.filter(name='format_time')
def format_time(value):
        # Assuming the input format is "%Y-%m-%dT%H:%M"
        time = value.split('T')[1]
        # time = value[1]
        return (time)
    
@register.filter(name='format_date')
def format_date(value):
        print(value)
        # Assuming the input format is "%Y-%m-%d"
        datetime_object = datetime.strptime(value, "%Y-%m-%dT%H:%M")
        # print(date)
        return(datetime_object)
  
@register.filter(name='format_date_flyshop')
def format_date_flyshop(value):
        print(value)
        # Assuming the input format is "%Y-%m-%d"
        datetime_object =  datetime.strptime(value, "%m/%d/%Y %H:%M")
        # print(date)
        return(datetime_object)   

@register.filter(name='format_duration')
def format_duration(total_hours):
    total_hours = float(total_hours)
    days = int(total_hours // 24)
    hours = int(total_hours % 24)
    minutes = round((total_hours % 1) * 60)

    result = ""
    if days:
        result += f"{days}d "
    if hours:
        result += f"{hours}h "
    if minutes:
        result += f"{minutes}m"

    return result.strip()

@register.filter(name='range_func')
def range_func(ietration):
    return range(0,int(ietration))


@register.filter(name='custommul')
def custommul(arg1, arg2):
    # Your tag logic here
    result = arg1 * arg2
    return result

@register.filter(name='format_datetime')
def format_datetime(value):
    try:
        # Assuming the input format is "%Y-%m-%dT%H:%M"
        return datetime.strptime(value, '%Y-%m-%dT%H:%M')
    except ValueError:
        return value



@register.filter(name='to_int')
def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return value
    
@register.filter(name='to_json')
def to_json(value):

    json_string = json.dumps(value)
    

    return json_string
    

@register.filter(name='single_format_duration')
def single_format_duration(total_hours):
    
    hours = int(total_hours // 60)
    minutes = int(total_hours % 60)

    result = ""
    if hours:
        result += f"{hours}h "
    if minutes:
        result += f"{minutes}m"

    return result.strip()

@register.filter(name='list_conv')
def list_conv(value):
    # print(value)
    # json_string = json.loads(value)
    json_string = value.split(",")
    return json_string
    
@register.filter(name='trans_load')
def trans_load(value):
    json_string = json.loads(value)
    # print(json_string)
    # json_string = value.split(",")
    return json_string

@register.filter(name='uniq_country')
def uniq_country(value):
    uniq_value =[]
    for i in value:
        if i["country"] not in uniq_value:
            uniq_value.append(i["country"])
   
    return uniq_value



@register.filter(name='uniq_city')
def uniq_city(value):
    uniq_value =[]
    for i in value:
        if i["city"] not in uniq_value:
            uniq_value.append(i["city"])
    
    return uniq_value
    


@register.filter(name='split_airline')
def split_airline(value):
    uniq_value = value.split('-')
    
    return uniq_value
    
@register.filter(name='time_hr')
def time_hr(minutes):

    hours = minutes // 60  # Get the whole hours
    remaining_minutes = minutes % 60
    time = str(hours)+"hr"+str(remaining_minutes)+"min" 
    return time


# @register.filter(name='add_comm_trpj_flights')
# def add_comm_trpj_flights(amount):
#     # print(amount,"xs")
#     comm = get_object_or_404(commision_tripjack,comm_type="TripJack_Flights")
#     new_comm = float(amount) * (float(comm.Commission)/100)
#     new_amount = amount + new_comm + (new_comm * 18/100)
#     # print(new_amount)
#     return new_amount

# @register.filter(name='add_comm_trpj_hotels')
# def add_comm_hotel(amount):
#     # print(amount,"xs")
#     comm = get_object_or_404(commision_tripjack,comm_type="TripJack_Hotel")
#     new_comm = float(amount) * (float(comm.Commission)/100)
#     new_amount = amount + new_comm + (new_comm * 18/100)
#     # print(new_amount)
#     return new_amount

@register.filter(name='non_stop')
def non_stop(i):

    if i == 0:
        return "Non"
    else:
        return i

@register.filter(name='reverse_tax')
def reverse_tax(amount):
    new_amount = float(amount) - float(amount) / 1.18
    formatted_value = '{:,.2f}'.format(new_amount) 
    return formatted_value

@register.filter(name='custom_divide')
def custom_divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return None