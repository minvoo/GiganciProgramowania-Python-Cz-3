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

def get_weather_info(lat, lon):
    response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&limit=1&appid={API_KEY}&lang=PL&units=metric')
    response_json = response.json()
    weather = response_json['weather'][0]['description']
    temperature = response_json['main']['temp']
    pressure = response_json['main']['pressure']
    humidity = response_json['main']['humidity']
    return weather, temperature, pressure, humidity

def get_country_full_name(country_code):
    #https://pastebin.com/TLFUr52y
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    country_name = response.json()[0]['translations']['pol']['common']
    return country_name

def get_currency_code(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"   # to samo co wyzej
    response = requests.get(url)
    currency_code = list(response.json()[0]['currencies'].keys())[0]
    return currency_code

def get_ratio(curr):
    if curr != "PLN":
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{curr.lower()}/"
        response = requests.get(url)
        ratio = response.json()['rates'][0]['mid']
    else:
        ratio = 1
    return ratio

def get_currency_ratio(ori_curr, dest_curr):   #np . ori_curr = PLN, dest_curr = EUR
    
    ori_ratio = get_ratio(ori_curr)
    dest_ratio = get_ratio(dest_curr)
    
    ratio = float(ori_ratio)/float(dest_ratio)
    return ratio


#https://pastebin.com/CXB6jDGS
print("INTELIGENTNY ASYSTENT PODROZY")
origin_city = input("Podaj miasto z ktorego podrozujesz (po angielsku) ")
d_city  = input("Podaj miasto do ktorego podrozujesz (tez po angielsku) ")

origin_lat, origin_lon, origin_city, origin_country = check_coordinates(origin_city, API_KEY)
destination_lat, destination_lon, destination_city, destination_country = check_coordinates(d_city, API_KEY)
weather, temperature, pressure, humidity = get_weather_info(destination_lat, destination_lon)
ori_curr = get_currency_code(origin_country)
dest_curr = get_currency_code(destination_country)
ratio = get_currency_ratio(ori_curr,dest_curr)
print(f'Miasto z ktorego podrozujesz: {origin_city}')
print(f'Lezy w kraju {get_country_full_name(origin_country)}')
print(f'Obowiazujaca waluta to : {ori_curr}')
print(f'Miasto do ktorego podrozujesz: {destination_city}')
print(f'Lezy w kraju {get_country_full_name(destination_country)}')
print(f'Obowiazujaca waluta to : {dest_curr}')
print(f"Średni kurs {ori_curr} na {dest_curr} to {ratio}")
print(f'Wspolrzedne geograficzne miasta do ktorego podrozujesz to: {destination_lat} szer.g., {destination_lon} dl.g.')
print(f'Pogoda: {weather} ')
print(f'Temperatura: {temperature}')
print(f'Wilgotnosc: {humidity}')
print(f'Cisnienie: {pressure}hPa')
# https://pastebin.com/xUg0q3Rb
