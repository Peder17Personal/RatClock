import os
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Absolute path to your DB
DB_FILE = r"C:\Users\LassePedersen\Documents\GitHub\RatClock\mark1\alarms.db"

# Ensure the table exists
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Alarms (
                Alarm_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Description TEXT,
                Time TEXT
            )
        """)
        conn.commit()

init_db()

@app.route("/api/alarms", methods=["GET"])
def get_alarms():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Alarms")
        rows = cursor.fetchall()
        alarms = [{"id": row[0], "description": row[1], "time": row[2]} for row in rows]
        return jsonify(alarms)

@app.route("/api/alarms", methods=["POST"])
def add_alarm():
    data = request.get_json()
    description = data.get("description")
    time = data.get("time")
    
    # Validate time format HH:MM
    import re
    if not re.match(r"^\d{2}:\d{2}$", time):
        return jsonify({"error": "Invalid time format"}), 400
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Alarms (Description, Time) VALUES (?, ?)", (description, time))
        conn.commit()
        return jsonify({"message": "Alarm added"}), 201

@app.route("/")
def index():
    return "RatClock API running"

if __name__ == "__main__":
    app.run(debug=True)
