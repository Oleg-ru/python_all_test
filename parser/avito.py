from bs4 import BeautifulSoup
import requests
from requests import get
import time
import random

url = 'https://www.avito.ru/lipetsk/kvartiry/sdam-ASgBAgICAUSSA8gQ?p='
houses = []
count = 1
while count <= 5:
    url = 'https://www.avito.ru/lipetsk/kvartiry/sdam-ASgBAgICAUSSA8gQ?p=' + str(count)
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_data = html_soup.find_all('div', class_="iva-item-body-KLUuy")
    if house_data != []:
        houses.extend(house_data)
        value = random.random()
        scale_value = 1 + (value * (9 - 5))
        print(scale_value)
        time.sleep(scale_value)
    else:
        print('empty')
        break
    count += 1

print(len(houses))
print(houses[0])
print()
n = int(len(houses)) - 1
count = 0
#