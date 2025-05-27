import requests
import os
from send_email import send_email
from datetime import datetime, timedelta

KEYWORD = "Eurovision"
NEWS_MAX_LIMIT = 10

date_yesterday = (datetime.today()-timedelta(days=1)).strftime("%Y-%m-%d")

# Create the request
url = ("https://newsapi.org/v2/everything?"
       f"q={KEYWORD}&"
       "searchIn=title,description&"
       "sortBy=publishedAt&"
       f"from={date_yesterday}&"
       f"apiKey={os.getenv("NEWS_API_KEY")}")

# Send the request and get the response
response = requests.get(url)
response_content = response.json()
articles = response_content["articles"][:NEWS_MAX_LIMIT]

# Parse the response and create the email's content
message = f"Subject: Yesterday's {KEYWORD} News\n\n"

if articles:
    for index, article in enumerate(articles):
        if article["title"] is not None:
            message += (str(index + 1) + " - "
                        + article["title"] + "\n"
                        + article["description"] + "\n"
                        + article["publishedAt"].split("T")[1][:-1] + "\n"
                        + article["url"] + 2 * "\n")
else:
    message += "No News :("

message = message.encode("UTF-8")

# Send the email
send_email(message)