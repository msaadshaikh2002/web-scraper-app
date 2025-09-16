import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Step 1: Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["scraping_db"]              # Database name
collection = db["products"]             # Collection name
collection.delete_many({})              # Optional: Clear old data

# Step 2: Scrape the website
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('article', class_='product_pod')

# Step 3: Insert into MongoDB
for product in products:
    name = product.find('h3').find('a')['title']
    price = product.find('p', class_='price_color').text

    product_data = {
        "name": name,
        "price": price
    }

    collection.insert_one(product_data)
    print(f"Stored: {name} - {price}")
