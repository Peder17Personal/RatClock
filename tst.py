import time
import threading

def alarm_clock(target_hour):
    while True:
        current_hour = time.localtime().tm_hour
        if current_hour == target_hour:
            print("wake up")
            break
        time.sleep(60)  # Check every minute

def run_in_background(target_hour):
    alarm_thread = threading.Thread(target=alarm_clock, args=(target_hour,))
    alarm_thread.daemon = True
    alarm_thread.start()

# Set the target hour (24-hour format)
target_hour = 7  # Change this to your desired hour
run_in_background(target_hour)

# Keep the main program running
while True:
    time.sleep(1)