import pprint
import profile
from pymongo import MongoClient
import car_options
from  print_options import line
from multipledispatch import dispatch
client = MongoClient("mongodb+srv://dj46:Mbas2014@cluster0.fusui.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
cars = client.login.cars
information = client.login.information 
def get_profile(user):
    name = user['username']
    profile = information.find_one({'username': name})
    return profile
#displays the whole garage, meaning all cars are displayed

def view_garage(user):
    profile = get_profile(user)
    car_inventory = profile["car_inventory"]
    length = len(car_inventory)
    parse = 0
    print("Displaying your garage\n")
    while parse < length:
        car = car_inventory[parse]
        if len(car) == 0:
            parse += 1
            continue
        print("-----------------------------------------------")
        print("car#:  ",parse)
        print(car['year'], car['make'], car['model'])
        print("speed: ", car['speed'])
        print("acceleration: ", car['acceleration'])
        print("handling: ", car['handling'])
        print("valuation of your car: ", car['value'])
        print("-----------------------------------------------")
        parse += 1
    line()
def View_garage(car_inventory,num):
    length = len(car_inventory)
    parse = 0
    print("Displaying your garage\n")
    while parse < length:
        car = car_inventory[parse]
        if len(car) == 0:
            parse += 1
            continue
        print("-----------------------------------------------")
        print("car#:  ",parse)
        print(car['year'], car['make'], car['model'])
        print("speed: ", car['speed'])
        print("acceleration: ", car['acceleration'])
        print("handling: ", car['handling'])
        print("valuation of your car: ", car['value'])
        print("-----------------------------------------------")
        parse += 1
    line()
def print_option(user,option):
    name = user['username']
    profile = information.find_one({'username': name})
    car_inventory = profile["car_inventory"]
    #grab instance of car_inventory
    choice = car_options.which_carTwo(car_inventory)
    if choice == None:
        return
    car = car_inventory[choice]
    
    if len(car) == 0:
        print("no car here")
        print(" ")
        line()
        return 
    else:
        print_option = car[option]
        line()
        print("\nthe ", option ,"of your: ")
        print(car['year'], car['make'], car['model'])
        print("is...", print_option,"\n")
        line()
def display_onlycars(car_inventory):
    length = len(car_inventory)
    parse = 0
    print("Displaying your garage\n")
    while parse < length:
        car = car_inventory[parse]
        if len(car) == 0:
            parse += 1
            continue
        print("-----------------------------------------------")
        print("car#:  ",parse)
        print(car['year'], car['make'], car['model'])
        print("-----------------------------------------------")
        parse += 1
    line()     
def display_upgrades(user):
    profile = get_profile(user)
    line()
    print("dislaying engine package installed: ",profile['engine upgrade'])
    print("dislaying suspension upgrade installed: ",profile['suspension upgrade'])
    print("dislaying cosmetic upgrade installed: ",profile['exterior upgrade'])
    line()
    
