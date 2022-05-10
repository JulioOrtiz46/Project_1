from pymongo import MongoClient

from print_options import line
client = MongoClient("mongodb+srv://dj46:Mbas2014@cluster0.fusui.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#print(client.list_database_names())
#this will be used to 
login_database = client.login
user_collection = login_database.users
information = login_database.Information

#login will login the user to the game if they have a user created, and having a matching parit
#of username and password combination
#will return True or False depending on the

#overloading login method
def login(find):
    if (user_collection.find_one(find )):
        print("Success")
        line()
        line()
        return True
    else:
        print("user not created or credentials not correct!")
        return False
#createuser() will be used to create a brand new user to store information, will also create a unique username
def createuser(user):
    users = login_database.users
    users.insert_one(user)

#delete user will take in two inputs, a username and a password, if there two matching pairs
#then it will delete the user 
def deleteuser():
    find = find_user()
    login_status = login(find)
    if (login_status):
        user_collection.delete_one(find)
        info = login_database.information
        username = find['username']
        info.delete_one({"username": username})
    else:
        print("")
        return
#find_user method wll be used for the deleteuser and login methods, this method will return a dictionary
#with the credentials of the user for each action
def find_user():
    user = input("Username:")
    password = input("password:")
    find = {
            'username': user,
            'password': password
        }
    return find
   

