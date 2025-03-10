import time
import datetime

def set_alarm(alarm_time, alarm_day):
    while True:
        current_time = datetime.datetime.now()
        current_day = current_time.strftime("%A")
        current_time_str = current_time.strftime("%H:%M")

        print(f"Current time: {current_time_str}", "\t target time", alarm_time, "\t current day", current_day, "\t target day", alarm_day)

        if  alarm_day == current_day and current_time_str == alarm_time:
            print("Wake up! It's time!")
            return True

        time.sleep(30)  # Check every 30 seconds


def alarm(Name, day, time, recurrence, snooze, setting):
    

if __name__ == "__main__":
    alarm_time = "10:00"
    alarm_day = "Sunday"
    set_alarm(alarm_time, alarm_day)