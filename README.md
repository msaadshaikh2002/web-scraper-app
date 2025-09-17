# Web Scraping App (Python + MongoDB + Flask)

A beginner-friendly web app that scrapes product data (name + price) from [books.toscrape.com](http://books.toscrape.com), stores it in MongoDB, and displays the results in a Flask web UI.

## Features

- Scrapes book titles and prices using `requests` + `BeautifulSoup`
- Stores data in a MongoDB collection using `pymongo`
- Displays scraped data using a Flask web app
- Clean HTML table view of products

## Technologies Used

- Python 3
- Flask
- MongoDB
- BeautifulSoup
- Requests
- HTML (Jinja2 templates)

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/web-scraper-app.git
cd web-scraper-app