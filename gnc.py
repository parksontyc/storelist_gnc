import requests
from bs4 import BeautifulSoup
import time
import csv

store_name = []
store_address = []

url = "https://www.gnc.com.tw/zh/stores"

res = requests.get(url, timeout=2)

html = res.text

soup = BeautifulSoup(html.replace("\n", "").strip(), "html.parser")

items = soup.find_all('div', class_="col-sm-6 col-md-4 mb-4 pb-2 store-locator__list__item")

for item in items:
	store_name.append(item.find('a', class_="text--bold store-locator__list__item__name text--dark text-decoration-none").text)
	store_address.append(item.find('p').text)
	
with open('storelist_gnc.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市名稱', '門市地址']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_name[n])
        newrow.append(store_address[n])
        csvwriter.writerow(newrow)
