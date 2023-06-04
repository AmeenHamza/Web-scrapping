import pandas as pd
import requests
from bs4 import BeautifulSoup

url = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.969670000000065&lon=-118.249935#.Y2H7_3bMLIU')

soup = BeautifulSoup(url.content,'html.parser')
weeks = soup.find(id='seven-day-forecast-body')
# print(week) 

# items_original = week.find_all('div',class_='tombstone-container') # Aese bhi ek hi baat h
items = weeks.find_all(class_='tombstone-container') # Aese bhi ek hi baat h

# print((items[0]))
period_days = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]
# print(period_days)
# print(short_desc)
# print(temperature)

weather_des = pd.DataFrame({
    'period' : period_days,
    'short des' : short_desc,
    'TEmperature' : temperature
})

print(weather_des)

# Save this file into csv file
weather_des.to_csv('F:\weather.csv')