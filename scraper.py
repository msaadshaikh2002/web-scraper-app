import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["scraping_db"]
collection = db["products"]
collection.delete_many({})

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('article', class_='product_pod')

for product in products:
    name = product.find('h3').find('a')['title']
    price = product.find('p', class_='price_color').text

    product_data = {
        "name": name,
        "price": price
    }

    collection.insert_one(product_data)
    print(f"Stored: {name} - {price}")
