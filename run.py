"""
Main function of the program.
Reads URLs from a file and scrapes data from each URL,
then saves the scraped data to individual files.
"""

import sys
from module_1.web_scraper import WebScraper
from module_2.file_handler import FileHandler

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 run.py <path_to_urls_file>")
        return

    input_file = sys.argv[1]
    with open(input_file, "r") as file:
        urls = file.readlines()

    web_scraper = WebScraper()
    file_handler = FileHandler()

    for idx, url in enumerate(urls, start=1):
        url = url.strip()
        # Scrape data from the URL
        headline, body_texts, author, timestamp = web_scraper.scrape(url)
        # Save the processed data to a file
        file_handler.save_to_file(idx, url, headline, body_texts, author, timestamp, output_dir="Data/processed")
        # Save the raw HTML content to a file
        file_handler.save_raw_html(idx, url, output_dir="Data/raw")

if __name__ == "__main__":
    main()