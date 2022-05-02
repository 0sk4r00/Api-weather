import requests

API_KEY = '25684a358d8be109dbd3985a6055d52f'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
LOCATION_URL='http://api.openweathermap.org/geo/1.0/direct?'
city = input('Enter the city: ')
limit = input("Enter limit: ")

def get_cities(name,limit):
    location_url = f"{LOCATION_URL}q={city}&limit={limit}&appid={API_KEY}"
    location_response = requests.get(location_url)
    if location_response.status_code == 200:
        dane = location_response.json()
        return (dane)
    else:
        print("Error Occurred")

def show_weather(name,limit):
    dane = get_cities(name,limit)
    for miasto in dane:
        request_url = f"{BASE_URL}?lat={miasto['lat']}&lon={miasto['lon']}&appid={API_KEY}"
        response = requests.get(request_url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = round(data["main"]["temp"] - 273.15,2)
            print(f"Weather {weather} Temperature: {temperature}, celsius in {miasto['country']}")
        else:
            print("An error occurred.")

show_weather(city,limit)


