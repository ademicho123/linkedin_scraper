import requests
from bs4 import BeautifulSoup
import csv

def scrape_articles(url, keyword=None):
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
        if keyword is None or keyword.lower() in title.lower():
            data.append({"title": title, "link": article_url})

    return data

def save_to_csv(data, filename):
    # Write the data to a CSV file
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(data)

# URL of the webpage
url = "https://www.linkedin.com/pulse/topics/home/?trk=content-hub-home-page_guest_nav_menu_articles"

# Specify the keyword (e.g., "machine learning") or set it to None to retrieve all articles
keyword = None

# Scrape articles based on the keyword
articles_data = scrape_articles(url, keyword)

# Save the scraped articles to a CSV file
save_to_csv(articles_data, "articles.csv")
