
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime

# Replace with your actual service account key file path
cred = credentials.Certificate("C:/Users/LassePedersen/Documents/GitHub/RatClock/ratclock-59c8f-firebase-adminsdk-gsxkf-be6f53df8c.json")

# Get your Realtime Database URL from the Firebase console
database_url = "https://ratclock-59c8f-default-rtdb.europe-west1.firebasedatabase.app/"

firebase_admin.initialize_app(cred, {
    'databaseURL': database_url
})

# Reference to your Realtime Database
database = db.reference('/')

def read(searchElement = 'NO'):
    #We read all the data and then sort/filter. Should be changed for effeciency and speed. 
    
    data = database.get()
    print(data)

    
    if(searchElement == 'NO'):
        data = database.get()
    
        print(len(data))

        if(len(data) == 0 ):
            print("SearchElement empty")
    else:
        print("Not Empty")
    
    return data

def write(DB = 'AlarmTime', data_name = 'tomorrow', data_value = 'NAN'):
    database.child(DB).set({ data_name : data_value })


    


read('YES')

