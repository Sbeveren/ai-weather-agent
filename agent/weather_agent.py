import requests
import time
from .config import API_KEY, CITY, OUTFILE

class WeatherAgent:
    def __init__(self, api_key=API_KEY, city=CITY, outfile=OUTFILE):
        self.api_key = api_key
        self.city = city
        self.outfile = outfile

    def sense(self):
        """Fetch weather data from OpenWeatherMap API."""
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={self.city}&appid={self.api_key}&units=metric"
        )
        response = requests.get(url)
        data = response.json()
        # Debug: print API response
        print("API Response:", data)
        return data

    def think(self, data):
        """Process the API data into a human-readable summary."""
        if "weather" not in data or "main" not in data:
            return f"Error: API response invalid. Full response: {data}\n"
        try:
            condition = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            summary = (
                f"Weather Summary for {self.city}:\n"
                f"- Condition: {condition}\n"
                f"- Temperature: {temp}°C\n"
                f"- Humidity: {humidity}%\n"
                f"- Timestamp: {time.ctime()}\n"
                "--------------------------------------\n"
            )
            return summary
        except Exception as e:
            return f"Error processing data: {e}\n"

    def act(self, summary):
        """Write the summary to the log file using UTF-8 encoding."""
        with open(self.outfile, "a", encoding="utf-8") as f:
            f.write(summary)

    def run(self):
        """Perform one agent cycle."""
        data = self.sense()
        summary = self.think(data)
        self.act(summary)
        print("Agent cycle completed.")