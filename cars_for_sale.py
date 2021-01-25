import requests
from bs4 import BeautifulSoup

url = 'https://www.truecar.com/used-cars-for-sale/listings/acura/mdx/location-andover-ma/'

make = input("MAKE: ").lower()
model = input("MODEL: ").lower()
city = str(input("CITY: ")).lower()
state = input("STATE ABBREVIATION: ").lower()

url = str(f"https://www.truecar.com/used-cars-for-sale/listings/{make}/{model}/location-{city}-{state}/")

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
cars_full = soup.find_all(class_='margin-top-3 d-flex flex-grow col-md-6 col-xl-4')

for car_full in cars_full:
    car_link = car_full.find(class_='card card-1 card-shadow card-shadow-hover vehicle-card _1qd1muk')
    car_content = car_full.find(class_='card-content vehicle-card-body')
    year = car_content.find(class_='vehicle-card-year font-size-1')
    car_type = car_content.find(class_='font-size-1 text-truncate')
    price = car_content.find(class_='heading-3 margin-y-1 font-weight-bold')
    miles_away = car_content.find(class_='vehicle-card-location font-size-1 margin-top-1')
    mileage = car_content.find(class_='font-size-1 text-truncate')
    color = car_content.find(class_='vehicle-card-location font-size-1 margin-top-1 text-truncate')
    history = car_content.find(class_='vehicle-card-location font-size-1 margin-top-1')
    history_milesaway = car_content.find_all(class_='vehicle-card-location font-size-1 margin-top-1')
    for history_mile in history_milesaway:
        if "accident" in history_mile.text:
            history = history_mile
        elif "mi -" in history_mile.text:
            miles_away = history_mile
        else:
            pass
    deal = car_content.find(
        class_='graph-icon-title margin-left-1 vehicle-card-price-rating-label text-truncate font-weight-bold')
    cartype_mileage = car_content.find_all(class_='font-size-1 text-truncate')
    for cartype_mile in cartype_mileage:
        if "miles" in cartype_mile.text:
            mileage = cartype_mile
        elif "price" in cartype_mile.text:
            pass
        else:
            car_type = cartype_mile
    print('')
    try:
        print(year.text)
    except:
        print("year not found")
    try:
        print(mileage.text)
    except:
        print("Mileage not found")
    try:
        print(car_type.text)
    except:
        print("Car model not found")
    try:
        print(color.text)
    except:
        print("Car color not found")
    try:
        print(history.text)
    except:
        print("Car history not found")
    try:
        print(miles_away.text)
    except:
        print("Location not found")
    try:
        print(price.text)
    except:
        print("Price not found")
    try:
        print(deal.text)
    except:
        print("Deal not found")
    try:
        print('https://www.truecar.com' + car_link.attrs['href'])
    except:
        print("Link not found")
    print('')