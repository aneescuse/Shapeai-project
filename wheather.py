# -*- coding: utf-8 -*-
"""Wheather.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11gslxsC-dsXLHVjBP13xSW7ajZUAGskc

**Wheather Condition using api and Saving as text File**



---
"""

import requests
#import os
from datetime import datetime

api_key = 'c57c3f4440c060a707d26646cde201b4'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

with open('weather.txt','w') as f:
  f.write("----------------------------------------------------------------"+"\n")
  f.write("Weather Stat for - {} ~ {}".format(location.upper(), date_time)+"\n\n")
  f.write("Current temparature is :"+str(temp_city)+" deg c"+"\n\n")
  f.write("Current Wheather : "+str(weather_desc)+"\n\n")
  f.write("Current Humidity : "+str(hmdt)+"\n\n")
  f.write("Current Wind speed : "+str(wind_spd)+"\n\n")
  f.write("----------------------------------------------------------------")

"""# New Section"""