#module that contains the methods that will allow the user to buy a new car
import car_options
from print_options import line
from car_options import get_car_attributes
#this is going to print the menu, when called will diplay the contents of the dictionary menu_options

#this method will look at the text file that has the menu of cars
#and will print it out
def read_file():
    with open('listofcars.txt') as f:
        line = f.read()
        cleansed = line.replace('"', '')
        cleansed = cleansed.replace(',', ' ')
        cleansed = cleansed.replace(':', ' ---')
        print(cleansed)

#this is the method that will perfrom the attempt to buy a new car
def buy_car(user,option):
    #contain the attributes of the car the user would like to purchase
    car_shell = get_car_attributes(option)
    #this will grab the current users balance,using the get_balanc command from car_options
    balance = car_options.get_balance(user) 
    #this creates a variable that stores the value of the new car the user would like to purchase
    value = car_shell['value']
    
    #if statement to determine if the user can afford the new car
    if value < balance:
                #if its is then it subtracts the price(value) from the balance
                new_balance = balance - value
                #adds the car to the users inventory
                car_options.add_car(user,car_shell,new_balance) 
    else:
        #if they dont then this prints out
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
        if 0 < option < 11:
            buy_car(user,option)  
        elif option == 11:
            print('Exiting...')
            line()
            break
        else:
            print('Invaled option, please enter a number between 1 and 10')
            print("")