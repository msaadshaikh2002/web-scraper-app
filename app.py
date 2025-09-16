from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["scraping_db"]
products_collection = db["products"]

@app.route('/')
def home():
    products = list(products_collection.find())
    return render_template("home.html", products=products)

if __name__ == '__main__':
    app.run(debug=True)
