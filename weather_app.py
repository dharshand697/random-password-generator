import requests

API_KEY = "c01a8d406a61de035531dfa848f74691"  # <-- Replace with your actual OpenWeatherMap API key

def fetch_weather(city: str):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}  # use metric units for easier reading
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data: dict, city: str):
    if data.get("cod") != 200:
        print(f"Error: {data.get('message', 'Could not fetch data')}")
        return

    main = data["main"]
    weather_desc = data["weather"][0]["description"].capitalize()
    temp = main["temp"]
    humidity = main["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather in {city}:")
    print(f" • Description : {weather_desc}")
    print(f" • Temperature : {temp}°C")
    print(f" • Humidity    : {humidity}%")
    print(f" • Wind Speed  : {wind_speed} m/s")

def main():
    city = input("Enter city name: ").strip()
    data = fetch_weather(city)
    display_weather(data, city)

if __name__ == "__main__":
    main()
