#system admin LPE
#Service API GIT, WeatherAPI, News


                        #import section
import datetime



def get_current_time():
    # Get the current time
    current_time = datetime.now()
    # Format the time for better readability
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

def main():

    # Call the function and print the current time
    print("Current Time:", get_current_time())
    print("Test")

    if __name__ == "__main__":
        main()
