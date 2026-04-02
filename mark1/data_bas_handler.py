import sqlite3

DB_FILE = "alarms.db"

def init_db():
    try:
        # Connect (creates DB file if it does not exist)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create table if it does not exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Alarms (
                Alarm_ID INTEGER PRIMARY KEY,
                Description TEXT,
                Time TIME,
                Date DATE,
                Repeatition TEXT,
                Pre_alarm TEXT,
                Alarm_logic TEXT,
                Post_alarm TEXT,
                Enable BOOLEAN
            )
        """)

        conn.commit()
        print("Database initialized successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if conn:
            conn.close()

def add_alarm(description, time, date, repetition, pre_alarm, alarm_logic, post_alarm, enable):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Alarms (Description, Time, Date, Repeatition, Pre_alarm, Alarm_logic, Post_alarm, Enable)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (description, time, date, repetition, pre_alarm, alarm_logic, post_alarm, enable))

        conn.commit()
        print("Alarm added successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if conn:
            conn.close()

def delete_alarm(alarm_id):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Alarms WHERE Alarm_ID = ?", (alarm_id,))
        conn.commit()
        print("Alarm deleted successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if conn:
            conn.close()

def get_next_alarm():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM Alarms
            WHERE Enable = 1
            ORDER BY Date, Time
            LIMIT 1
        """)
        alarm = cursor.fetchone()
        return alarm

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if conn:
            conn.close()

def get_all_alarms():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Alarms")
        alarms = cursor.fetchall()
        return alarms

    except sqlite3.Error as e:
        print(f"Database error: {e}") 
        return []

    finally:
        if conn:
            conn.close()

def dummy_data_insert():
    add_alarm("Morning Alarm", "07:00:00", "2024-07-01", "Daily", "5 minutes before", "Standard", "Snooze for 10 minutes", True)
    add_alarm("Meeting Reminder", "14:00:00", "2024-07-01", "None", "10 minutes before", "Standard", "No snooze", True)
    add_alarm("Workout Alarm", "18:00:00", "2024-07-01", "Weekly", "15 minutes before", "Standard", "Snooze for 5 minutes", True)
    add_alarm("Medication Reminder", "09:00:00", "2024-07-01", "Daily", "30 minutes before", "Standard", "No snooze", True)
    add_alarm("Bedtime Alarm", "22:00:00", "2024-07-01", "Daily", "1 hour before", "Standard", "Snooze for 15 minutes", True)

def check_for_updates():
    # Placeholder for update checking logic
    pass

if __name__ == "__main__":
    init_db()
    a = get_next_alarm()
    print(a)