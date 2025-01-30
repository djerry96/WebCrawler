import os
import requests
from bs4 import BeautifulSoup

def crawl(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, 'html.parser')
        with open('links.txt', 'w') as file:
            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    file.write(href + '\n')
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    url = os.getenv("URL")
    if url:
        crawl(url)
    else:
        print("No URL provided. Set the URL environment variable.")
