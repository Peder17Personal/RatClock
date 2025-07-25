import threading
import time
from datetime import datetime, timedelta
import json
import pygame

import alarm_function

# Global variables
alarm_time = None
alarm_active = True
exit_flag = False
scheduler_running = False
last_reload_date = None
schedule = []
lock = threading.Lock()


stop_flag = False

def play_alarm(file_path):
    global stop_flag
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops=-1)  # Loop indefinitely

    while not stop_flag:
        time.sleep(1)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

def clock_thread():
    global alarm_time, alarm_active, exit_flag, schedule, scheduler_running, last_reload_date
    while not exit_flag:
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M")
        today = now.strftime("%A")
        current_time = now.strftime("%H:%M")

        with lock:
            # Reload alarm schedule at 04:00 if not already reloaded today
            if current_time == "04:00" or current_time == "04:01" and (last_reload_date != now.date()):
                try:
                    with open("alarmScheduel.json", "r") as f:
                        data = json.load(f)
                    schedule.clear()
                    for entry in data["alarms"]:
                        schedule.append((
                            entry["day"],
                            entry["time"],
                            entry.get("enabled", True),
                            entry.get("repeat", True)
                        ))
                    print("🔄 Alarm schedule reloaded at 04:00")
                    last_reload_date = now.date()
                except Exception as e:
                    print(f"Failed to reload schedule at 04:00: {e}")

            if alarm_active and alarm_time:
                alarm_time_str = alarm_time.strftime("%Y-%m-%d %H:%M")
                if now_str >= alarm_time_str:
                    print("\n⏰ Alarm ringing! Type 'snooze' or 'exit'")
                    alarm_active = False
                    threading.Thread(target=play_alarm, args=("sound.mp3",)).start()

            # Trigger scheduled alarms if running
            if scheduler_running:
                for day, time_str, enabled, repeat in schedule:
                    if day == today and time_str == current_time and enabled:
                        alarm_function.play_local_alarm(1)  # Play local alarm
                        print(f"🔔 Scheduled alarm for {day} at {time_str} is ringing")
                        break

        time.sleep(30)


def terminal_thread():
    global alarm_time, alarm_active, exit_flag, scheduler_running, schedule
    print("Welcome to the Alarm Clock!")

    while not exit_flag:
        cmd = input(">> ").strip().lower()
        with lock:
            if cmd == "exit":
                exit_flag = True
                print("Exiting alarm clock.")

            elif cmd.startswith("set"):
                try:
                    parts = cmd.split()
                    if len(parts) != 3:
                        raise ValueError
                    _, _, hhmm = parts

                    now = datetime.now()
                    target_time = datetime.strptime(hhmm, "%H:%M").replace(
                        year=now.year, month=now.month, day=now.day, second=0, microsecond=0
                    )
                    if target_time <= now:
                        target_time += timedelta(days=1)

                    alarm_time = target_time
                    alarm_active = True

                    time_diff = alarm_time - now
                    hours, remainder = divmod(int(time_diff.total_seconds()), 3600)
                    minutes, _ = divmod(remainder, 60)

                    print(f"🕒 One-time alarm set for {alarm_time.strftime('%Y-%m-%d %H:%M')} "
                          f"({hours}h {minutes}min from now)")
                    
                    # upload alarm to alameScheduel.json
                    try:
                        with open("alarmScheduel.json", "r") as f:
                            data = json.load(f)
                    except FileNotFoundError:
                        data = {"alarms": []}
                    except json.JSONDecodeError:
                        print("Error reading alarm schedule file. Please check the JSON format.")
                        return
                    

                except ValueError:
                    print("❌ Invalid format. Use: set time HH:MM")

            elif cmd == "snooze":
                if alarm_time:
                    alarm_time = datetime.now() + timedelta(minutes=5)
                    alarm_active = True
                    print(f"Snoozed until {alarm_time.strftime('%H:%M')}")
                else:
                    print("No alarm to snooze.")

            elif cmd == "start":
                try:
                    with open("alarmScheduel.json", "r") as f:
                        data = json.load(f)

                    if "alarms" not in data:
                        print("No 'alarms' key found in JSON.")
                        continue

                    schedule = []
                    for entry in data["alarms"]:
                        day = entry["day"]
                        time_str = entry["time"]
                        enabled = entry.get("enabled", True)
                        repeat = entry.get("repeat", True)
                        schedule.append((day, time_str, enabled, repeat))
                        print(f"Loaded alarm: {day}, {time_str}, enabled: {enabled}, repeat: {repeat}")

                    scheduler_running = True
                    print("✅ Scheduler started.")

                except FileNotFoundError:
                    print("Alarm schedule file not found.")
                except Exception as e:
                    print(f"Error loading schedule: {e}")

            elif cmd == "stop":
                scheduler_running = False
                print("⏹️ Scheduler stopped.")

            elif cmd == "help":
                print("Alarm Clock Help:")
                print("Commands:")
                print("  start       → Load and start scheduled alarms")
                print("  stop        → Stop scheduled alarms")
                print("  set HH:MM   → Set one-time alarm")
                print("  snooze      → Snooze current alarm for 5 minutes")
                print("  exit        → Exit the program")
                print("  help        → Show this help message")

            elif cmd == "status":
                if alarm_time:
                    print(f"Current alarm time: {alarm_time.strftime('%Y-%m-%d %H:%M')}")
                else:
                    print("No active alarm set.")
                print(f"Scheduler running: {'Yes' if scheduler_running else 'No'}")
                print(f"Alarm active: {'Yes' if alarm_active else 'No'}")

            elif cmd == "time":
                now = datetime.now()
                print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

            else:
                print("❓ Unknown command. Type 'help' for available commands.")

def main():
    t1 = threading.Thread(target=clock_thread)
    t2 = threading.Thread(target=terminal_thread)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
