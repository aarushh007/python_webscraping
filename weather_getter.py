import requests
from bs4 import BeautifulSoup
import csv
import time
import os

page = requests.get('https://cutt.ly/Kh2dHVN')

soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

if os.path.exists("./weather.csv"):
  os.remove("./weather.csv")

f = open('weather.csv', 'a', newline='')
for item in items:
    time_period = item.find(class_='period-name')
    short_desc = item.find(class_='short-desc')
    temp = item.find(class_='temp')
    temp_text = temp.text[0:-3]
    temp_text += ' F'
    tup = (time_period.text, short_desc.text, temp_text)
    writer = csv.writer(f)
    writer.writerow(tup)
    print('')
    print(time_period.text)
    print(short_desc.text)
    print(temp_text)
    print('')

f.close()

