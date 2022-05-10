#module that contains the methods that will login/delete/create users
import car_options
from print_options import line
import upgrade_menu
import garage_menu
import buying_menu
#this is going to print the menu, when called will diplay the contents of the dictionary menu_options
def print_menu():
    menu_options = {
    1: 'View your inventory',
    2: 'Upgrade you car',
    3: 'Sell your car',
    4: 'Buy another car',
    5: 'View balance',
    6: 'Exit'
}
    for key in menu_options.keys():
        print(key, '---', menu_options[key])

def car_menu(user):
#a simple loop menu that take in numbers as inputs for options on the menu
    while(True):
        line()
        print_menu()
        line()
        option = ''
        try:
            option = int(input("enter your choice"))
        except:
            print('Wrong input. please leave a number')
            line()
        #checks the input option for one of the OPTIONS on the menu
        if option == 1:
            print('Sending to your garage...')
            print("")
            garage_menu.garage_menu(user)
        elif option == 2:
            print('Sending to shop...')
            print("")
            upgrade_menu.upgrade_menu(user)
        elif option == 3:
            print('sell your car initiated...')
            print("")
            test = car_options.auction(user)
        elif option == 4:
            print('Buying car selected...')
            print("")
            buying_menu.car_menu(user)
        elif option == 5:
            print('Viewing your balance...')
            print("")
            balance = car_options.get_balance(user)
            print(balance)
            line()
        elif option == 6:
            print('Exiting...')
            break
        else:
            print('Invaled option, please enter a number between 1 and 4')
