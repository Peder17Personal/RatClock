import data_base_handler as db


next_alarm = db.get_next_alarm()

if next_alarm:
    print(next_alarm)

dataSet = (1, 'Morning Alarm', '07:00', '2024-07-01', 'Daily', '5 minutes before', 'Standard', 'Snooze for 10 minutes', 1)

