import requests
import os
from send_email import send_email

url = "https://newsapi.org/v2/everything?q=eurovison&sortBy=publishedAt&apiKey=" + os.getenv("NEWS_API_KEY")

req = requests.get(url)
content = req.json()

message = ""
for index, article in enumerate(content["articles"]):
    message += (str(index) + " - "
                + article["title"] + "\n"
                + article["description"] + 2 * "\n")

message = message.encode("UTF-8")
send_email(message)