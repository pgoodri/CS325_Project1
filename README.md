# Web Scraper
This Python script is a simple web scraper that extracts information from a list of URLs provided in a file named 'urls.txt'. It retrieves the headline, body text, author, and timestamp of articles from each URL and saves this information into separate text files.

## How it Works
The script uses the 'requests' library to fetch the HTML content of each URL and the 'BeautifulSoup' library to parse the HTML and extract the desired information.

- The 'scrape' function takes a URL as input and returns the headline, body text, author, and timestamp extracted from the HTML content of the webpage.
- The 'save' function takes the extracted information and saves it into a text file. Each text file is named 'article{idx}.txt', where '{idx}' is a unique identifier corresponding to the order of the URLs in the 'urls.txt' file.
- The 'main' function reads the list of URLs from the 'urls.txt' file, iterates over each URL, scrapes the information using the 'scrape' function, and saves it using the 'save' function.

## Instructions
### Prerequisites
- Python 3.x installed on your system.
- Access to the internet to fetch webpages.

### Setup
1. Clone or download the repository containing the script.
2. Ensure you have the necessary libraries installed. You can install them using pip:
```
pip install requests beautifulsoup4
```

### Usage
1. Prepare a file named 'urls.txt' containing the URLs of the webpages you want to scrape. Each URL should be on a separate line.
2. Run the script 'web_scraper.py' using the following command:
```
python web_scraper.py
```
3. The script will scrape each webpage, extract the information, and save it into separate text files.
4. Once the script finishes execution, you will find the output text files in the same directory as the script.

## Example Output
Suppose 'urls.txt' contains the following URLs:
```
https://example.com/article1
https://example.com/article2
```
After running the script, the output files will be named as follows:

- 'article1.txt': Contains the information extracted from the first URL.
- 'article2.txt': Contains the information extracted from the second URL.

Each text file will include the URL, headline, body text, author, and timestamp of the corresponding article.

Feel free to customize the script or modify the input file to suit your specific needs.