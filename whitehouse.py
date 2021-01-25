from bs4 import BeautifulSoup
import requests
import os
import csv

page = requests.get('https://www.whitehouse.gov/briefings-statements/')
soup = BeautifulSoup(page.content, 'html.parser')

briefings = soup.find_all(class_='briefing-statement briefing-statement--results')

if os.path.exists('whitehouse.csv'):
    os.remove('whitehouse.csv')

f = open("whitehouse.csv", 'a', newline='')

for item in briefings:
    title_div = item.find(class_='briefing-statement__title')
    link_tag = title_div.find('a')
    link = link_tag.attrs['href']
    title = link_tag.text
    time_tag = item.find(class_='meta__date')
    time = time_tag.text
    print(time)
    print(title)
    print(link)
    print('')

    tup = (time, title, link)
    writer = csv.writer(f)
    writer.writerow(tup)

f.close()