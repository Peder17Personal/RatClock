import time
import datetime

def set_alarm(alarm_time, alarm_day):
    while True:
        current_time = datetime.datetime.now()
        current_day = current_time.strftime("%A")
        current_time_str = current_time.strftime("%H:%M")

        if current_day == alarm_day and current_time_str == alarm_time:
            print("Wake up! It's time!")
            break

        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    alarm_time = "21:26"
    alarm_day = "sunday"
    set_alarm(alarm_time, alarm_day)