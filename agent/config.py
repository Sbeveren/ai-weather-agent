import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Manila"
OUTFILE = "logs/weather_log.txt"
INTERVAL = 10

print("Loaded API_KEY:", API_KEY)  # Optional: check if it’s loaded