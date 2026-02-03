from bs4 import BeautifulSoup
import requests
import time
import random
from urllib.parse import urlparse, urljoin
import re
import csv

#Function that indexes the webpage
def index_page(webpage, webpage_url):

    #Collect title and description
    title_tag = webpage.find('title')
    title = title_tag.get_text().strip() if title_tag else 'No Title'

    #Collect description
    description = ''
    meta_description = webpage.find('meta', attrs={'name': 'description'})
    if meta_description and 'content' in meta_description.attrs:
        description = meta_description['content']
    else:
        text_content = webpage.get_text(separator=" ", strip=True)
        description = text_content[:200] + "..." if len(text_content) > 200 else text_content

    # Grab all the words in the page
    words = re.findall(r'\b\w+\b', webpage.get_text(separator=" ", strip=True).lower())

    # Double check and fliter out any numbers, symbols, etc
    # WE ONLY WANT WORDS
    words = [word for word in words if word.isalpha()]

    # Add the information to the index
    indexed_page = {
        "url": webpage_url,
        "title": title,
        "description": description,
        "words": words
    }
    return indexed_page

def web_crawler():
    # our list of urls
    urls = ["https://www.wikipedia.org/"]
    visited_urls = set()
    # Loops through the list of urls
    while urls:
        # grabs the next url
        current_url = urls.pop()
        print("time to crawl: " + current_url)
        time.sleep(random.uniform(1, 3))
        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to retrieve {current_url}: {e}")
            continue
        # grabbing the content of the page
        webpage = BeautifulSoup(response.content, "html.parser")

        # grabbing the links from the page
        hyperlinks = webpage.select("a[href]")
        # looping through the links and adding them to our list of urls
        for hyperlink in hyperlinks:
            url = hyperlink["href"]
            #Formats the url into a proper url
            if url.startswith("#"):
                continue
            if url.startswith("//"):
                parsed_url = urlparse(current_url)
                url = f"{parsed_url.scheme}:{url}"
            elif not url.startswith("http"):
                url = urljoin(current_url, url)
            url = url.split('#')[0]
            # If we havent visited this url yet, add it to our list
            if url not in visited_urls:
                urls.append(url)
                visited_urls.add(url)
