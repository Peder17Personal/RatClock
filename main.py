#system admin LPE
#Service API GIT, WeatherAPI, News

import json
                        #import section
import AlarmClock


def main():

    # Example usage of the AlarmClock module
    print("Setting alarm for 10:12 on Sunday")

    if AlarmClock.set_alarm("10:12", "Sunday"):
        print("Alarm set successfully")
    
    if __name__ == "__main__":
        main()
