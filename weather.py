import requests

from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

with open('weather.txt','w') as f:

    f.write("Weather Stats for - {} | {}\n".format(location.upper(), date_time))
    f.write("Current temperature is : {:.2f} deg C\n".format(temp_city))
    f.write("Current weather desc   : {}\n".format(weather_desc))
    f.write("Current Humidity       : {} %\n".format(hmdt))
    f.write("Current wind speed     : {} kmph\n".format(wind_spd))