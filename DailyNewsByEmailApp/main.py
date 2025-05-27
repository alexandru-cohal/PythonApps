import requests
import os
from send_email import send_email

topic = "eurovison"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "language=en&"
       f"apiKey={os.getenv("NEWS_API_KEY")}")

req = requests.get(url)
content = req.json()

message = "Subject: Today's news\n"
for index, article in enumerate(content["articles"][:20]):
    if article["title"] is not None:
        message += (str(index + 1) + " - "
                    + article["title"] + "\n"
                    + article["description"] + "\n"
                    + article["url"] + 2 * "\n")

message = message.encode("UTF-8")
send_email(message)