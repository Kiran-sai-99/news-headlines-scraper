# News Headlines Scraper (Python)

-A console-based Python project that scrapes the latest news headlines from Hacker News and saves them into a text file (headlines.txt).
-This project demonstrates the practical use of Python for web scraping, parsing HTML, handling errors, and storing data in a file. It is beginner-friendly, lightweight, and can be extended to scrape other websites as well.

# Features

- Fetches real-time news headlines from Hacker News
  The scraper connects to Hacker News and downloads the HTML content of the homepage. It extracts the latest headlines, giving you an up-to-date view of trending news and      tech topics.

- Extracts headlines using BeautifulSoup
  BeautifulSoup is a Python library that parses HTML and XML. The scraper finds all the headline elements (<span class="titleline">) and retrieves the text inside the links    (<a> tags). This allows us to collect the main news headlines in a clean, readable format.

- Saves headlines to a text file (headlines.txt)
  All fetched headlines are stored persistently in a text file. This makes it easy to access, share, or analyze the headlines later without needing to scrape the website       again.

- Displays the first 10 headlines in the terminal
  For quick reference, the scraper prints the top 10 headlines directly in the console. This makes it convenient to see trending news without opening a file.

- Lightweight and beginner-friendly
  The project requires only a few lines of code and minimal Python knowledge. It is a great starting point to learn web scraping, error handling, file I/O, and Python          programming best practices.


# Requirements

- Python 3.6+

- Python Libraries:

requests
 -> for sending HTTP requests to web pages

beautifulsoup4
 -> for parsing and navigating HTML

# Install dependencies using pip:
  -pip install requests beautifulsoup4

# How to Run

- Clone the repository
    - git clone https://github.com/Kiran-sai-99/news-headlines-scraper.git
    - cd news-headlines-scraper

- Run the scraper script
    - python scraper.py

# File Info

  - scraper.py -> Main Python script containing the scraping logic.
  - headlines.txt -> Auto-generated text file storing all scraped headlines.

# Concepts Learned

This project helps you understand and practice the following key programming concepts:

- Making HTTP requests in Python
    - Learn how to connect to websites, fetch their HTML content, and handle server errors.

- Parsing and navigating HTML
    - Understand the structure of a webpage and how to extract meaningful information using BeautifulSoup.

- File handling (read/write) in Python
    - Store scraped data in a persistent format (text file) safely and efficiently using with open().

- Error handling and program robustness
    - Learn how to use try/except to catch runtime errors (like network issues) and keep your script running smoothly.

- Avoiding duplicates and cleaning data
    - Ensure that only unique and valid headlines are stored, demonstrating good data-cleaning practices.

# Built With

- Python 3

- requests

- BeautifulSoup4
