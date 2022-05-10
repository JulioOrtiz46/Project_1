#module that contains the methods that will login/delete/create users
import print_options
import User_loginoptions
import car_menu_ 
import car_options
import print_options
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
    print_options.line()
    print_menu()
    print_options.line()
    option = ''
    try:
        option = int(input("enter your choice"))
    except:
        print('wrong input. please leave a number')
    #checks the input option for one of the OPTIONS on the menu
    if option == 1:
        print('Login Selected')
        #grab car_shell from car_id
        #looks at balance with if statement and sees if they can afford the car
        #if they can then go through with transaction
        user = User_loginoptions.find_user()
        status = User_loginoptions.login(user)
        if status:
            car_menu_.car_menu(user)
    elif option == 2:
        try:
            print('User Creation, please create a unique username')
            new_user = User_loginoptions.find_user()
            User_loginoptions.createuser(new_user)
            car_options.first_time(new_user)
            print_options.line()
        except:
            print("ERROR: username is taken")

    elif option == 3:
        print('Delete User Selected')
        User_loginoptions.deleteuser()
        print_options.line()
    elif option == 4:
        print('Exiting...')
        print("thank you for playing")
        print_options.line()
        print_options.line()
        exit()
    else:
        print('Invaled option, please enter a number between 1 and 4')
