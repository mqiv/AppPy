# from wsgiref import headers
from traceback import print_tb
import requests #для url запросов
from bs4 import BeautifulSoup  #для работы с html 

# sleep = 3 #время задержки 

# url = 'https://www.google.com/finance/markets/most-active'
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13904.16.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.25 Safari/537.36'
#  }
url = 'https://www.google.com/finance/markets/cryptocurrencies'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13904.16.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.25 Safari/537.36'
 }
req = requests.get(url, headers=headers)
src = req.text
# print(src)

#Запись в файл
# with open('index.html', 'w') as file:
#     file.write(src)

#Чтение из файла
# with open('index.html') as file:
#     src = file.read()

soup = BeautifulSoup(src, "html.parser")
all_product_name = soup.find('ul', class_='sbnBtf').find_all('div', class_='ZvmM7') #названия
all_product_price = soup.find('ul', class_='sbnBtf').find_all('div', class_='YMlKec') #цена на данный момент

for product_price in all_product_price:
    product_price_text = product_price.text
    # print(f'{product_price}')

for product_name in all_product_name:
    product_name_text = product_name.text
    # print(f'{product_name}')

for product_name_text, product_price_text in zip(all_product_name, all_product_price):
    print(f'{product_name_text.text}: {product_price_text.text}')

# print(soup.ul.li.a.prettify())