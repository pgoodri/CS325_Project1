"""
SOLID Principle Used: Open/Closed Principle (OCP)
Benefit: The module is open for extension (adding new functionalities) but closed for modification. This promotes flexibility, modularity, and reusability in the codebase.
"""

"""
Purpose of scrape():
    Scrapes data from the given URL.

Args:
    url (str): The URL of the webpage to scrape.

Returns:
    tuple: A tuple containing headline, body_texts, author, and timestamp.
"""

import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        pass
    
    def scrape(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        headline = (soup.find("h1")).get_text()
        body_elements = soup.findAll('p', class_='paragraph inline-placeholder')
        body_texts = (' '.join([element.get_text().strip().replace('/', '') for element in body_elements]))
        author = (soup.find('div', class_='byline__names')).get_text()
        timestamp = (soup.find('div', class_='timestamp')).get_text()

        return headline, body_texts, author, timestamp