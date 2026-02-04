from bs4 import BeautifulSoup
import requests
import time
import random
from urllib.parse import urlparse, urljoin
import re

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

def compute_pagerank(graph, damping_factor=0.85, max_iterations=100, tol=1.0e-6):
    # Build the set of all URLs
    all_nodes = set(graph.keys())
    for links in graph.values():
        all_nodes.update(links)
    num_nodes = len(all_nodes)
    # Initialize PageRank scores
    pagerank = {url: 1.0 / num_nodes for url in all_nodes}
    # Identify dangling nodes (nodes with no outgoing links)
    dangling_nodes = [url for url in all_nodes if url not in graph or len(graph[url]) == 0]
    # Iterative computation
    for iteration in range(max_iterations):
        new_pagerank = {}
        # Sum of PageRank scores from dangling nodes
        dangling_sum = damping_factor * sum(pagerank[node] for node in dangling_nodes) / num_nodes
        for url in all_nodes:
            rank = (1.0 - damping_factor) / num_nodes
            rank += dangling_sum
            # Sum contributions from incoming links
            for node in graph:
                if url in graph[node]:
                    out_degree = len(graph[node])
                    rank += damping_factor * pagerank[node] / out_degree
            new_pagerank[url] = rank
        # Check for convergence
        error = sum(abs(new_pagerank[url] - pagerank[url]) for url in all_nodes)
        if error < tol:
            print(f"Converged after {iteration + 1} iterations.")
            break
        pagerank = new_pagerank
    return pagerank

def web_crawler():
    # our list of urls
    urls = ["https://www.wikipedia.org/"]
    visited_urls = set()
    indexed_pages = []  # Store indexed pages
    graph = {}  # Store the link graph for PageRank
    
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
        
        # Index the page
        page_data = index_page(webpage, current_url)
        indexed_pages.append(page_data)
        print(f"Indexed: {page_data['title']}")
        
        # Initialize graph entry for current URL
        graph[current_url] = []

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
            # Add to graph
            graph[current_url].append(url)
    
    # Compute PageRank
    print("\nComputing PageRank...")
    pagerank_scores = compute_pagerank(graph)
    
    # Sort pages by PageRank
    sorted_pages = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)
    
    print("\nTop 10 pages by PageRank:")
    for i, (url, score) in enumerate(sorted_pages[:10], 1):
        print(f"{i}. {url}: {score:.6f}")
    
    return indexed_pages, graph, pagerank_scores

if __name__ == "__main__":
    web_crawler()
