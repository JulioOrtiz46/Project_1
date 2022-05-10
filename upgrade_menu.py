#module that contains the methods that will login/delete/create users
import car_options
import upgrade_options
from multipledispatch import dispatch
#this is going to print the menu, when called will diplay the contents of the dictionary menu_options
def print_menu():
    menu_options = {
    1: 'View engine upgrades',
    2: 'View Suspension Upgrades',
    3: 'View Exterior upgrades upgrades',
    4: 'Exit'
}
    for key in menu_options.keys():
        print(key, '---', menu_options[key])

def upgrade_menu(user):
#a simple loop menu that take in numbers as inputs for options on the menu
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input("enter your choice"))
        except:
            print('wrong input. please leave a number')
        #checks the input option for one of the OPTIONS on the menu
        if option == 1:
            print('Viewing engine upgrades')
            upgrade_options.package_menu(user,'engine')
        elif option == 2:
            print('Viewing suspension upgrades')
            upgrade_options.package_menu(user,'suspension')
            
        elif option == 3:
            print('Viewing Cosmetic packages')
            upgrade_options.package_menu(user,'cosmetic')
        elif option == 4:
            print('Exiting...')
            break
        else:
            print('Invaled option, please enter a number between 1 and 4')
