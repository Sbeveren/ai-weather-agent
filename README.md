## How to Run
1. Clone the repository:

```bash
git clone https://github.com/Sbeveren/ai-weather-agent.git
cd ai-weather-agent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a .env file in the project root:

```bash
WEATHER_API_KEY=your_actual_api_key_here
```

The API key used for this project is located in the Documentation.

4. Run the agent:

```bash
python main.py
```

The agent will log weather summaries to logs/weather_log.txt.

### Notes:
- Make sure your terminal/editor supports UTF-8 to correctly display the ° symbol.
- The logs folder and .env are ignored in Git via .gitignore to protect sensitive information and runtime files.