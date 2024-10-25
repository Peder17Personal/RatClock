import win32com.client
import pandas as pd

def get_calendar_events(start_date, end_date):
    outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
    calendar = outlook.GetDefaultFolder(9).Items
    calendar.IncludeRecurrences = True
    calendar.Sort('[Start]')
    calendar = calendar.Restrict("[Start] >= '{}' AND [End] <= '{}'".format(start_date, end_date))

    events = []
    for appointment in calendar:
        events.append({
            'Subject': appointment.Subject,
            'Start': appointment.Start,
            'End': appointment.End,
            'Location': appointment.Location
        })

    return pd.DataFrame(events)

# Example usage
events_df = get_calendar_events('2024-10-01', '2024-10-31')
print(events_df)