import requests
from pprint import pprint

API_KEY = "2f6124752d7f679da34ebfa1132eff3c"

#pozyskiwanie geolokalizacji 
def check_coordinates(city, API_KEY):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')
    #pprint(response.status_code)
    #pprint(response.json())
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    city = response.json()[0]['name']
    country = response.json()[0]['country']
    return lat, lon, city, country

def get_weather_info():
    response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&limit=1&appid={API_KEY}&lang=PL&units=metric')
    response_json = response.json()
    weather = response_json['weather'][0]['description']
    temperature = response_json['main']['temp']
    pressure = response_json['main']['pressure']
    humidity = response_json['main']['humidity']




print("INTELIGENTNY ASYSTENT PODROZY")
origin_city = input("Podaj miasto z ktorego podrozujesz (po angielsku) ")
d_city  = input("Podaj miasto do ktorego podrozujesz (tez po angielsku) ")

origin_lat, origin_lon, origin_city, origin_country = check_coordinates(origin_city, API_KEY)
destination_lat, destination_lon, destination_city, destination_country = check_coordinates(d_city, API_KEY)

print(f'Miasto z ktorego podrozujesz: {origin_city}')
print(f'Miasto do ktorego podrozujesz: {destination_city}')
print(f'Wspolrzedne geograficzne miasta do ktorego podrozujesz to: {destination_lat} szer.g., {destination_lon} dl.g.')

# https://pastebin.com/yCXsied4
