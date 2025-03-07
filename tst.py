import threading
import time
from datetime import datetime, timedelta

class AlarmClock:
    def __init__(self, alarm_time):
        self.alarm_time = alarm_time
        self.running = False

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def run(self):
        while self.running:
            current_time = datetime.now()
            print(f"Current time: {current_time.strftime('%H:%M:%S')}")
            if current_time >= self.alarm_time:
                print("Alarm! Time's up!")
                self.stop()
            time.sleep(1)

if __name__ == "__main__":
    alarm_time = "2025-03-07 14:01:00"  # Set alarm for 10 seconds from now
    print(alarm_time)
    alarm_clock = AlarmClock(alarm_time)
    alarm_clock.start()

    # Simulate other processes
    for i in range(5):
        print(f"Simulating other process {i+1}")
        time.sleep(2)