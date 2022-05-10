from heapq import merge
from secrets import choice
from xmlrpc.client import boolean
from pymongo import MongoClient
import car_menu_
import garage_option
from pprint import pprint
from print_options import line
client = MongoClient("mongodb+srv://dj46:Mbas2014@cluster0.fusui.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
cars = client.login.cars
information = client.login.information 
#this is the the methods that willl be used when an intial user is created, tehy will have the choice
#of three cars and one is chosen t start the game, they are given an intial amount of money that can
# be used to customize there car and later they can sell it to buy an upgraded car, and continue the game
"""-------------------------------------------------------------------------------------------------------"""
#this is the intial menu that the user will recieve
#this is a menu used to display the options of the first three inital cars used
#in the game
def car_menu():
    car_selector = {
        1: "2011 BMW M3",
        2: "2008 Lexus ISF",
        3: "2011 Mercedez C63 AMG"
    }
    print("Choose a starting car")
    for key in car_selector.keys():
        print(key, '---', car_selector[key])
# this is a input reader that will parse the users answer and dertermine if that is the right type of input
def input_reader():
    option = ' '
    #car_menu()
    while(True):
        try:
            option = int(input("enter your choice"))
        except:
            print('wrong input. please leave a number')
        #checks the input option for one of the OPTIONS on the menu 
        return option
#will use the option and recieve the car form the car database and return its attributes
def get_car_attributes(option):
    option += 100 # to match id on cars
    cars = client.login.cars
    shell = cars.find_one({"car_id": option})
    inital_car = {
        '_id' : shell['_id'],
        'year': shell['year'],
        'make': shell['make'],
        'model': shell['model'],
        'speed': shell['speed'],
        'acceleration': shell['acceleration'],
        'handling': shell['handling'],
        'value': shell['value']
    }

    return inital_car
def get_profile(user):
    name = user['username']
    profile = information.find_one({'username': name})
    return profile
def add_car(user,new_car,new_balance):
    #first get usernamer
    #find user from info
    profile = get_profile(user)
    #get car_inventory instance
    car_inventory = profile["car_inventory"]
    #get length() of car invernotry
    length = len(car_inventory)
    #get data of car_att based on id and store them in a object
    """new_car"""
    # create a query with set and put into users profile
    username = profile['username']
    query = {"username": username}
    
    key = "car_inventory." + str(length)

    values = { "$set" : { 
        key :  new_car
        } 
    }
    information.update_many( query, values )
    #update balance remove value from balance
    values = { "$set" : { 
        "balance" :  new_balance
        } 
    }
    information.update_many( query, values )
#first_car is the second method the user will interact with, they will be taken the the intial steps of choosing a first car and 
#its will create there user account
def first_car(new):
    car_menu() #will display the choices
    first_choice = input_reader()

    username = new["username"] #username will recieve the username used before and use it to link there account aswell, 
    firstcar = get_car_attributes(first_choice)
    new_user = {
        "username": username,  
        'engine upgrade': 0,
        'suspension upgrade': 0,
        'exterior upgrade': 0,
        'balance': 10000,
        'car_inventory': [firstcar]

    }  
    information.insert_one(new_user)

def first_time(new_user):
    #First usercreation will then be introduce to the objective with the help of introduction()
    first_car(new_user)
    car_menu_.car_menu(new_user)

def which_car(car_inventory):
    length = len(car_inventory)
    garage_option.View_garage(car_inventory,0)
    while True:
        
        try:
            choice = int(input("enter your choice"))
            print("")
            break
        except:
            print('wrong input. please leave a number')
            print(" ")
        #checks the input option for one of the OPTIONS on the menu   
    is_between =  0 <= choice < length
        #return number that was chosen - 1
    if(is_between == False):
            print("Not a option")
            line()
            return
    else:
            return choice 
    
def which_carTwo(car_inventory):
    length = len(car_inventory)
    garage_option.display_onlycars(car_inventory)
    while True:
        
        try:
            choice = int(input("enter your choice"))
            print("")
            break
        except:
            print('wrong input. please leave a number')
            print(" ")
        #checks the input option for one of the OPTIONS on the menu   
    is_between =  0 <= choice < length
        #return number that was chosen - 1
    if(is_between == False):
            print("Not a option")
            line()
            return
    else:
            return choice 
         

def auction(user):
    name = user['username']
    full = information.find_one({'username': name})
    car_inventory = full['car_inventory']
    choice = which_car(car_inventory) 
    if choice == None:
        return  
    car = car_inventory[choice]
    if len(car) == 0:
        print("No car here")
        line()
        return 0
    else:
        value = car['value']

        new_balance = full['balance']
        new_balance += value
        
        
        query = {"username": name}
        values = { "$set" : { 
            "balance" : new_balance, 
            "engine upgrade": 0,
            "suspension upgrade": 0,
            "exterior upgrade": 0
            } }
        
        information.update_one( query,values)
        address = "car_inventory."+ str(choice)
        values = { "$set" : { address : [] } }
        information.update_one( query, values )
        return 1

def get_balance(user):
    name = user['username']
    full = information.find_one({'username': name})
    balance = full['balance']
    return balance
