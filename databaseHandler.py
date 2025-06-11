import sqlite3
import argparse
import json
import sys

DB_NAME = "alarms.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alarms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alarm_time TEXT NOT NULL,
            alarm_date TEXT NOT NULL,
            title TEXT NOT NULL,
            scheduling TEXT NOT NULL,
            snooze BOOLEAN NOT NULL,
            sensors INTEGER NOT NULL,
            active BOOLEAN NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_dummy_data():
    conn = connect_db()
    cursor = conn.cursor()
    dummy_alarms = [
        ('07:00', '19-06-2025', 'Morning Alarm', 'Mon-Fri', True, 2, True),
        ('08:30', '20-06-2025', 'Weekend Wakeup', 'Sat-Sun', False, 1, False),
        ('06:45', '15-06-2025', 'Gym Day', 'Once:2025-06-15', True, 3, True),
        ('05:15', '21-06-2025', 'Early Hike', 'Sun', False, 2, True),
        ('09:00', '22-06-2025', 'Meeting Reminder', 'Once:2025-06-22', True, 1, True),
        ('10:30', '23-06-2025', 'Work Start', 'Mon-Fri', False, 2, True),
        ('12:00', '24-06-2025', 'Lunch Break', 'Mon-Fri', False, 0, True),
        ('15:00', '25-06-2025', 'Afternoon Alarm', 'Mon-Fri', True, 1, True),
        ('18:00', '26-06-2025', 'Evening Alarm', 'Daily', False, 1, True),
        ('21:00', '27-06-2025', 'Night Alarm', 'Daily', True, 0, False),
    ]
    cursor.executemany('''
        INSERT INTO alarms (alarm_time, alarm_date, title, scheduling, snooze, sensors, active)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', dummy_alarms)
    conn.commit()
    conn.close()
