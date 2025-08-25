import requests

API_KEY = "https://wttr.in/?format=j1"  # Free weather API, no key needed

city = "Bengaluru"
url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url).json()

# Extract temperature and weather
temp = response["current_condition"][0]["temp_C"]
desc = response["current_condition"][0]["weatherDesc"][0]["value"]

print(f"🌤️ Weather in {city}: {temp}°C, {desc}")
