import requests
import os

url = "https://newsapi.org/v2/everything?q=eurovison&sortBy=publishedAt&apiKey=" + os.getenv("NEWS_API_KEY")

req = requests.get(url)
content = req.json()

for article in content["articles"]:
    print(article["title"])