#system admin LPE
#Service API GIT, WeatherAPI, News

                        #import section
import AlarmClock

def main():
    if AlarmClock.set_alarm("10:12", "Sunday"):
        print("Alarm set successfully")
    
    if __name__ == "__main__":
        main()
