import requests
import datetime

def get_today_forecast(api_key):
    city_name = "Aarhus,DK"
    today = datetime.date.today()
    print("today:", today)
    print("city_name:", city_name)

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    data = response.json()
    forecasts = data.get("list", [])

    today_forecasts = [
        entry for entry in forecasts
        if datetime.datetime.fromtimestamp(entry["dt"]).date() == today
    ]

    if not today_forecasts:
        return "No forecast data found for today."

    output = f"Forecast for Aarhus, Denmark on {today}:\n"
    for entry in today_forecasts:
        time_str = datetime.datetime.fromtimestamp(entry["dt"]).strftime("%H:%M")
        temp = entry["main"]["temp"]
        desc = entry["weather"][0]["description"]
        output += f"  - {time_str}: {temp:.1f}°C, {desc}\n"

    return output

# Example usage
if __name__ == "__main__":
    api_key = "126ceea2fc6945910fe44a6e47fb7432"  # Replace with your actual key
    print(get_today_forecast(api_key))
