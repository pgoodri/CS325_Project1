"""
SOLID Principle Used: Open/Closed Principle (OCP)
Benefit: The module is open for extension (adding new functionalities) but closed for modification. This promotes flexibility, modularity, and reusability in the codebase.
"""

"""
Purpose of save_to_file():
    Saves scraped data to a file.

Args:
    idx (int): Index of the article.
    url (str): The URL of the webpage.
    headline (str): Headline of the article.
    body_texts (str): Body text of the article.
    author (str): Author of the article.
    timestamp (str): Timestamp of the article.
    output_dir (str): Directory to save the file.
"""

"""
Purpose of save_raw_html():
    Saves raw HTML content to a file.

Args:
    idx (int): Index of the webpage.
    url (str): The URL of the webpage.
    raw_html (str): Raw HTML content of the webpage.
    output_dir (str): Directory to save the file.
"""

import requests

class FileHandler:
    def __init__(self):
        pass

    def save_to_file(self, idx, url, headline, body_texts, author, timestamp, output_dir):
        filename = f"{output_dir}/article{idx}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"URL: {url}\n\n")
            file.write(f"Headline: {headline}\n") 
            file.write(f"Body: {body_texts}\n\n")
            file.write(f"Author: {author}\n")
            file.write(f"Timestamp: {timestamp}\n\n")

    def save_raw_html(self, idx, url, output_dir):
        filename = f"{output_dir}/raw_{idx}.html"
        response = requests.get(url)
        raw_html = response.text
        with open(filename, "w", encoding="utf-8") as file:
            file.write(raw_html)