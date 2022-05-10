#module that contains the methods that will login/delete/create users
import car_options
from print_options import line
import upgrade_menu
import garage_menu
from car_options import get_car_attributes
import print_options
#this is going to print the menu, when called will diplay the contents of the dictionary menu_options

def read_file():
    with open('listofcars.txt') as f:
        line = f.read()
        cleansed = line.replace('"', '')
        cleansed = cleansed.replace(',', ' ')
        cleansed = cleansed.replace(':', ' ---')
        print(cleansed)

def buy_car(user,option):
    car_shell = get_car_attributes(option)
    balance = car_options.get_balance(user) 
    value = car_shell['value']
    if value < balance:
                new_balance = balance - value
                car_options.add_car(user,car_shell,new_balance) 
    else:
        print("Not enough in balance")
        line()
              
def car_menu(user):  
#a simple loop menu that take in numbers as inputs for options on the menu
    
    while(True):
        line()
        read_file()
        line()
        option = ''
        try:
            option = int(input("Enter your choice"))
            print("")
        except:
            print('Wrong input. please leave a number')
            print("")
        #checks the input option for one of the OPTIONS on the menu
        if option == 1:
            buy_car(user,option)  
        elif option == 2:
            buy_car(user,option)     
        elif option == 3:
            buy_car(user,option)  
        elif option == 4:
            buy_car(user,option)
        elif option == 5:
            buy_car(user,option)
        elif option == 6:
            buy_car(user,option)
        elif option == 7:
            buy_car(user,option)
        elif option == 8:
            buy_car(user,option)
        elif option == 9:
            buy_car(user,option)
        elif option == 10:
            car_shell = get_car_attributes(option)  
            car_options.add_car(user,car_shell)  
        elif option == 11:
            print('Exiting...')
            line()
            break
        else:
            print('Invaled option, please enter a number between 1 and 4')
            print("")