import json


def get_alarm_schedule():

    try:
        with open('alarm_schedule.json', 'r') as file:
            schedule = json.load(file)
        return schedule
    except FileNotFoundError:
        print("Alarm schedule file not found. Returning empty schedule.")
        return {}

def set_alarm_schedule(schedule):
    try:
        with open('alarm_schedule.json', 'w') as file:
            json.dump(schedule, file)
            print("Alarm schedule updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating alarm schedule: {e}")
        return False
    print("Alarm stopped.")

def main():
    # Example usage
    schedule = get_alarm_schedule()
    #print("Current Alarm Schedule:", schedule)

    
    
if __name__ == "__main__":
    main()
