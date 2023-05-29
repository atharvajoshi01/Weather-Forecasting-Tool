import requests
import json

API_KEY = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(weather_data):
    if weather_data is None:
        print("Failed to fetch weather data.")
    else:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")

city = input("Enter city name: ")
weather_data = get_weather(city)
display_weather(weather_data)
