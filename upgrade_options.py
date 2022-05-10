#module that contains the methods that will login/delete/create users
from inspect import Attribute
from msilib.schema import Upgrade
from multiprocessing.sharedctypes import Value
from pprint import pprint
import profile
import User_loginoptions
import car_options
from pymongo import MongoClient
from multipledispatch import dispatch

from print_options import line
client = MongoClient("mongodb+srv://dj46:Mbas2014@cluster0.fusui.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
cars = client.login.cars
information = client.login.information 
#this is going to print the menu, when called will diplay the contents of the dictionary menu_options
def print_menu():
    menu_options = {
    1: 'Package 1',
    2: 'Package 2',
    3: 'Package 3',
    4: 'Exit'
}
    for key in menu_options.keys():
        print(key, '---', menu_options[key])
def get_username(user):
   username = user['username'] 
   return username
def get_choice(username):
    user_profile = information.find_one({"username" : username})
    car_inventory = user_profile['car_inventory']
    choice = car_options.which_carTwo(car_inventory)
    return choice
def get_car_inventory(username,choice):
    user_profile = information.find_one({"username" : username})
    car_inventory = user_profile['car_inventory']
    car_object = car_inventory[choice]#later the 0 can be subsitituted for different length car
    return car_object
    
def  get_car_id(car_inventory):
    car_id  = car_inventory["_id"]
    return car_id
def get_car_attribute(car_id):
    car_model = cars.find_one({'_id': car_id})
    return car_model
def engine_upgrade(car,package):
    #will take the numbered option they have chosen and return the new values based on the upgrade they chose, and then
#return the car object
    speed = car['speed']
    accelaration = car['acceleration']
    handling = car['handling']
    value = car['value']
    price = 0
    if package == 1:
        speed += 1.0
        accelaration += 1.0
        handling -= 1.0
        price = (speed + accelaration + handling) * 200
        value += value
        car['speed'] = speed
        car['acceleration'] = accelaration
        car['handling'] = handling
        car ['value'] = value
        #add the price and package to change the attributes in there profile
        car['price'] = price
        car['package'] = package
        upgrade_choice = "engine upgrade"
        car['upgrade choice'] = upgrade_choice
    #same for option2,3
    if package == 2:
        speed += 2.2
        accelaration += 3.5
        handling -= 2.5
        price = (speed + accelaration + handling) * 200
        value += price
        car['speed'] = speed
        car['acceleration'] = accelaration
        car['handling'] = handling
        car ['value'] = value
        car['price'] = price
        car['package'] = package
        upgrade_choice = "engine upgrade"
        car['upgrade choice'] = upgrade_choice
    if package == 3:
        speed += 4.2
        accelaration += 2.8
        handling -= 3.0
        price = (speed + accelaration + handling) * 200
        value += price
        car['speed'] = speed
        car['acceleration'] = accelaration
        car['handling'] = handling
        car ['value'] = value
        
        car['price'] = price
        car['package'] = package
        upgrade_choice = "engine upgrade"
        car['upgrade choice'] = upgrade_choice
    return car
def suspension_upgrade(car,package):
    #will take the numbered option they have chosen and return the new values based on the upgrade they chose, and then
#return the car object
    speed = car['speed']
    accelaration = car['acceleration']
    handling = car['handling']
    value = car['value']
    if package == 1:
        accelaration += 1
        handling += 3
        price = (speed + accelaration + handling) * 100
        value += price
        car['speed'] = speed
        car['acceleration'] = accelaration
        car['handling'] = handling
        car ['value'] = value
        
        car['price'] = price
        car['package'] = package
        upgrade_choice = "suspension upgrade"
        car['upgrade choice'] = upgrade_choice
    #same for option2,3
    if package == 2:
        speed += 1
        accelaration += 1.5
        handling += 4.5
        price = (speed + accelaration + handling) * 100
        value += price
        car['speed'] = speed
        car['acceleration'] = accelaration
        car['handling'] = handling
        car ['value'] = value
    
        car['price'] = price
        car['package'] = package
        upgrade_choice = "suspension upgrade"
        car['upgrade choice'] = upgrade_choice
    if package == 3:
        speed += 1
        accelaration += 2
        handling += 5.5
        price = (speed + accelaration + handling) * 100
        value += price
        car['speed'] = speed
        car['acceleration'] = accelaration
        car['handling'] = handling
        car ['value'] = value
        
        car['price'] = price
        car['package'] = package
        upgrade_choice = "suspension upgrade"
        car['upgrade choice'] = upgrade_choice
    return car
def cosmetic_upgrade(car,package):
    #will take the numbered option they have chosen and return the new values based on the upgrade they chose, and then
#return the car object
    speed = car['speed']
    accelaration = car['acceleration']
    handling = car['handling']
    value = car['value']
    if package == 1:
        speed -= 1
        accelaration -= 1
        handling += 1
        price = (speed + accelaration + handling) * 70
        value += price
        car['speed'] = speed
        car['acceleration'] = accelaration
        car['handling'] = handling
        car ['value'] = value
        
        car['price'] = price
        car['package'] = package
        upgrade_choice = "exterior upgrade"
        car['upgrade choice'] = upgrade_choice
    #same for option2,3
    if package == 2:
        speed -= 1.5
        accelaration -= -1
        handling += 2.5
        price = (speed + accelaration + handling) * 70
        value += price
        car['speed'] = speed
        car['acceleration'] = accelaration
        car['handling'] = handling
        car ['value'] = value
        
        car['price'] = price
        car['package'] = package
        upgrade_choice = "exterior upgrade"
        car['upgrade choice'] = upgrade_choice
        
    if package == 3:
        speed -= 2
        accelaration -= 2
        handling -= 3.5
        price = (speed + accelaration + handling) * 70
        value += price
        car['speed'] = speed
        car['acceleration'] = accelaration
        car['handling'] = handling
        car ['value'] = value
        
        car['price'] = price
        car['package'] = package
        upgrade_choice = "exterior upgrade"
        car['upgrade choice'] = upgrade_choice
        
    return car
def send_to_info(user,upgraded_car,choice):
    username = get_username(user)
    query = {"username": username}

    #create an instance of the profiles info, to change the attributes of 
    profile_info = information.find_one({'username': username})

    while True:
        try:
            balance = profile_info['balance'] - upgraded_car['price'] 
            if balance < 0:
                raise ValueError
            break
        except ValueError:
            print("Insuffient funds")
            return 0
    
    ci = "car_inventory." + str(choice)
    values = { "$set" : { 
        upgraded_car['upgrade choice'] : upgraded_car['package'],
        "balance" : balance,
        ci+".speed" : upgraded_car['speed'],
        ci+".acceleration" : upgraded_car['acceleration'],
        ci+".handling" : upgraded_car['handling'],
        ci+".value": upgraded_car['value']    
        } }
    information.update_many( query, values ) 
    return 1
    
def upgrade(user,choice,package):
    username = get_username(user)
    car_choice = get_choice(username)
    if car_choice == None:
        return
    car_inventory = get_car_inventory(username,car_choice)
    
    
    car_id = get_car_id(car_inventory)
    car_att = get_car_attribute(car_id)
    
    
    if choice == 'engine':
        upgraded_car = engine_upgrade(car_att,package)
    if choice == 'suspension':
        upgraded_car = suspension_upgrade(car_att,package)
    if choice == 'cosmetic':
        upgraded_car = cosmetic_upgrade(car_att,package)
    
    num = send_to_info(user,upgraded_car,car_choice)
    print("Succesfully Installed!")
    line()
    
def package_menu(user,choice):
#a simple loop menu that take in numbers as inputs for options on the menu
    while(True):
        print_menu()
        package = ''
        try:
            package = int(input("enter your choice"))
        except:
            print('wrong input. please leave a number')
        #checks the input option for one of the OPTIONS on the menu
        if package == 1:
            print('Package 1 selected!')
            #will get the car_id from the users username and retireve it form the server to avoid any gamebreaking errors 
            #then will get the uprade save them to a object and then updated to the user saved object in there account on the 
            #information databadse
            upgrade(user,choice,package)
        elif package == 2:
            upgrade(user,choice,package)
        elif package == 3:
            upgrade(user,choice,package)
        elif package == 4:
            print('Exiting...')
            break
        else:
            print('Invaled option, please enter a number between 1 and 4')