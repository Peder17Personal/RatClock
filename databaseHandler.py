import sqlite3
import argparse
import json
import sys

DB_NAME = "alarms.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def list_alarms():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alarms")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    conn.close()
    for row in rows:
        print(dict(zip(columns, row)))

def add_alarm(args):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO alarms (alarm_time, title, scheduling, snooze, sensors, active)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (args.time, args.title, args.scheduling, args.snooze, args.sensors, args.active))
    conn.commit()
    conn.close()
    print("Alarm added.")

def delete_alarm(args):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alarms WHERE id = ?", (args.id,))
    conn.commit()
    conn.close()
    print(f"Alarm with ID {args.id} deleted.")

def export_json():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alarms")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    conn.close()
    data = [dict(zip(columns, row)) for row in rows]
    print(json.dumps(data, indent=2))

def main():
    parser = argparse.ArgumentParser(description="Alarm CLI Tool")
    subparsers = parser.add_subparsers(dest='command')

    # list
    subparsers.add_parser("list", help="List all alarms")

    # add
    add = subparsers.add_parser("add", help="Add a new alarm")
    add.add_argument("--time", required=True, help="Alarm time in HH:MM format")
    add.add_argument("--title", required=True, help="Alarm title")
    add.add_argument("--scheduling", required=True, help="Scheduling info")
    add.add_argument("--snooze", type=bool, default=False, help="Snooze enabled (True/False)")
    add.add_argument("--sensors", type=int, default=0, help="Number of sensors")
    add.add_argument("--active", type=bool, default=True, help="Is the alarm active?")

    # delete
    delete = subparsers.add_parser("delete", help="Delete alarm by ID")
    delete.add_argument("--id", type=int, required=True, help="ID of alarm to delete")

    # export
    subparsers.add_parser("export", help="Export all alarms to JSON")

    args = parser.parse_args()

    if args.command == "list":
        list_alarms()
    elif args.command == "add":
        add_alarm(args)
    elif args.command == "delete":
        delete_alarm(args)
    elif args.command == "export":
        export_json()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
