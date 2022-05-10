from http import client
from pymongo import MongoClient

client = MongoClient("mongodb+srv://dj46:Mbas2014@cluster0.fusui.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#print(client.list_database_names())
#this will be used to 
login_collection = client.login
user_collection = login_collection.users

#login will login the user to the game if they have a user created, and having a matching parit
#of username and password combination
#will return True or False depending on the
 
def login():
    find = find_user()
    if (user_collection.find_one(find)):
        print("success")
        return True
    else:
        print("user not created or credentials not correct!")
        return False
#overloading login method

def login(find):
    if (user_collection.find_one(find )):
        print("success")
        return True
    else:
        print("user not created or credentials not correct!")
        return False
#createuser() will be used to create a brand new user to store information, will also create a unique username
def createuser():
    users = login_collection.users
    username = input("choose a username")
    password = input("Choose a password") 
    user = {
        "username": username,
        "password": password
    }
    users.insert_one(user)
#delete user will take in two inputs, a username and a password, if there two matching pairs
#then it will delete the user 
def deleteuser():
    find = find_user()
    login_status = login(find)
    if (login_status):
        user_collection.delete_one(find)
    else:
        exit()
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
   

