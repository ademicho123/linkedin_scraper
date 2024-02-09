import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage
url = "https://www.linkedin.com/pulse/topics/home/?trk=content-hub-home-page_guest_nav_menu_articles"

# Fetch the webpage content
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all article links in the page
article_links = soup.find_all("a", class_="min-w-0 !no-underline babybear:w-full")

# Store the data
data = []

# Iterate over each article link to extract title and link
for link in article_links:
    title = link.find("h2", class_="mb-1").get_text(strip=True)
    article_url = link["href"]
    data.append({"title": title, "link": article_url})

# Write the data to a CSV file
with open("articles.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerows(data)