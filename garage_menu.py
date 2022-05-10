import garage_option
from print_options import line
def print_menu():
    menu_options = {
    1: 'View all cars',
    2: 'View Speed',
    3: 'View Accellaration',
    4: 'View Handling',
    5: "View Installed Packages",
    6: "Exit"
}
    for key in menu_options.keys():
        print(key, '---', menu_options[key])

def garage_menu(user):
    #a simple loop menu that take in numbers as inputs for options on the menu
    while(True):
        line()
        print_menu()
        line()
        option = ''
        try:
            option = int(input("enter your choice"))
        except:
            print('wrong input. please leave a number')
        #checks the input option for one of the OPTIONS on the menu
        if option == 1:
            print('Viewing all cars....')
            garage_option.view_garage(user)
        elif option == 2:
            print('viewing speed...')
            num = garage_option.print_option(user,'speed')
        elif option == 3:
            print('viewing acceleration...')
            num =garage_option.print_option(user,'acceleration')
        elif option == 4:
            print('viewing handling...')
            num = garage_option.print_option(user,'handling')
        elif option == 5:
            garage_option.display_upgrades(user)
        elif option == 6:
            print("\n now exiting your garage...")
            break
        else:
            print('Invaled option, please enter a number between 1 and 4')   
