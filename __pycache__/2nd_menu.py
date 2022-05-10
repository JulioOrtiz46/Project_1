#module that contains the methods that will login/delete/create users
import User_loginoptions
import car_menu

#this is going to print the menu, when called will diplay the contents of the dictionary menu_options
def print_menu():
    menu_options = {
    1: 'Login',
    2: 'Create User',
    3: 'Delete User',
    4: 'Exit'
}
    for key in menu_options.keys():
        print(key, '---', menu_options[key])

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
        print('Login Selected')
        status = User_loginoptions.login()
        if status:
            car_menu.game_menu()
    elif option == 2:
        print('User Creation, please create a unique username')
        new_user = User_loginoptions.find_user()
        User_loginoptions.createuser(new_user)
        car_menu.first_time(new_user)

    elif option == 3:
        print('Delete User Selected')
        User_loginoptions.deleteuser()
    elif option == 4:
        print('Exiting...')
        print("thank you for playing")
        exit()
    else:
        print('Invaled option, please enter a number between 1 and 4')
