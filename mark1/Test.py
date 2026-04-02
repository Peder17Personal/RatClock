import data_base_handler as db


next_alarm = db.get_next_alarm()

if next_alarm:
    print("Next Alarm:")
    print(f"ID: {next_alarm[0]}")
    print(f"Date: {next_alarm[1]}")
    print(f"Time: {next_alarm[2]}")
    print(f"Enable: {next_alarm[3]}")

