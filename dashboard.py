# dashboard.py
import threading
import tkinter as tk
from tkinter import messagebox
from Alarm_core import set_alarm, snooze_alarm, start_scheduler, stop_scheduler, alarm_time, clock_thread, exit_flag

def build_dashboard():
    def on_set_alarm():
        time_str = entry_time.get()
        try:
            formatted = set_alarm(time_str)
            lbl_status.config(text=f"Alarm set for {formatted}")
        except:
            messagebox.showerror("Invalid time", "Use format HH:MM")

    def on_snooze():
        snooze_alarm()
        lbl_status.config(text=f"Alarm snoozed to {alarm_time.strftime('%H:%M')}")

    def on_start():
        start_scheduler()
        lbl_status.config(text="Scheduler started")

    def on_stop():
        stop_scheduler()
        lbl_status.config(text="Scheduler stopped")

    root = tk.Tk()
    root.title("Alarm Dashboard")

    tk.Label(root, text="Set Alarm (HH:MM):").grid(row=0, column=0, padx=5, pady=5)
    entry_time = tk.Entry(root)
    entry_time.grid(row=0, column=1, padx=5, pady=5)

    tk.Button(root, text="Set", command=on_set_alarm).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(root, text="Snooze", command=on_snooze).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(root, text="Start Scheduler", command=on_start).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="Stop Scheduler", command=on_stop).grid(row=1, column=2, padx=5, pady=5)

    lbl_status = tk.Label(root, text="Status: Waiting...")
    lbl_status.grid(row=2, column=0, columnspan=3, pady=10)

    root.protocol("WM_DELETE_WINDOW", lambda: [setattr(exit_flag, True), root.destroy()])
    threading.Thread(target=clock_thread, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    build_dashboard()
