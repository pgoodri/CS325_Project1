import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    headline = (soup.find("h1")).get_text()
    body_elements = soup.findAll('p', class_='paragraph inline-placeholder')
    body_texts = (' '.join([element.get_text().strip().replace('/', '') for element in body_elements]))
    author = (soup.find('div', class_='byline__names')).get_text()
    timestamp = (soup.find('div', class_='timestamp')).get_text()

    return headline, body_texts, author, timestamp

def save(idx, url, headline, body_texts, author, timestamp):
        filename = f"article{idx}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"URL: {url}\n\n")
            file.write(f"Headline: {headline}\n") 
            file.write(f"Body: {body_texts}\n\n")
            file.write(f"Author: {author}\n")
            file.write(f"Timestamp: {timestamp}\n\n")

def main():
    with open("urls.txt", "r") as file:
        urls = file.readlines()

    for idx, url in enumerate(urls, start=1):
        url = url.strip()
        headline, body_texts, author, timestamp = scrape(url)
        save(idx, url, headline, body_texts, author, timestamp)


if __name__ == "__main__":
    main()