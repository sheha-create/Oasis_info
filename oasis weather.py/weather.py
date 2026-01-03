 #Weather Application using OpenWeatherMap API
# Internship Project - OIBSIP
# Author: Your Name
# Description: Fetches and displays current weather information for a city

import requests


API_KEY = "ba134696a34ca3e2d58da0d5cb5826b1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


def display_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("\n--- Weather Report ---")
    print(f"Location : {city}, {country}")
    print(f"Temperature : {temperature} °C")
    print(f"Humidity : {humidity}%")
    print(f"Condition : {description.capitalize()}")


def main():
    print("\n=== Weather Application ===\n")

    while True:
        city = input("Enter city name: ").strip()

        if not city:
            print("City name cannot be empty.")
            continue

        weather_data = get_weather(city)

        if weather_data and weather_data.get("cod") == 200:
            display_weather(weather_data)
        else:
            print("Unable to fetch weather data. Check city name or API key.")

        choice = input("\nCheck weather for another city? (yes/no): ").lower()
        if choice != "yes":
            print("\nThank you for using the Weather App.")
            break


if __name__ == "__main__":
    main()
