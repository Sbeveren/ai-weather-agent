import time
from agent.weather_agent import WeatherAgent
from agent.config import INTERVAL

def main():
    agent = WeatherAgent()

    print("Starting AI Agent...\n")

    for _ in range(5):  # You can increase the number of cycles
        agent.run()
        time.sleep(INTERVAL)

    print("\nAgent finished running.")

if __name__ == "__main__":
    main()