# Web Crawler with PageRank

A Python-based web crawler that recursively discovers and indexes web pages, then ranks them using the PageRank algorithm.

## Features

- **Recursive crawling**: Automatically discovers and follows links from web pages
- **Page indexing**: Extracts and stores title, description, and word content from each page
- **PageRank calculation**: Implements Google's PageRank algorithm to rank pages by importance
- **Graph building**: Constructs a link graph showing relationships between pages
- **Polite crawling**: Implements random delays between requests to avoid overwhelming servers
- **URL normalization**: Handles relative URLs, protocol-relative URLs, and fragments
- **Error handling**: Gracefully handles failed requests and continues crawling

## Requirements

- Python 3.6+
- BeautifulSoup4
- requests

## Installation

1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install beautifulsoup4 requests
```

## Usage

Run the crawler:

```bash
python main.py
```

By default, the crawler starts at `https://www.wikipedia.org/` and will continue crawling links it discovers. After crawling completes, it will compute PageRank scores and display the top 10 ranked pages.

### Customizing the Starting URL

Edit the `urls` list in the `web_crawler()` function:

```python
urls = ["https://your-starting-url.com/"]
```

### Customizing PageRank Parameters

You can adjust the PageRank algorithm parameters by modifying the call to `compute_pagerank()`:

```python
pagerank_scores = compute_pagerank(
    graph,
    damping_factor=0.85,    # Probability of following links (0-1)
    max_iterations=100,      # Maximum iterations before stopping
    tol=1.0e-6              # Convergence threshold
)
```

## How It Works

1. **Crawling**: The crawler maintains a queue of URLs to visit and a set of already-visited URLs to avoid duplicates

2. **Indexing**: For each page visited, the `index_page()` function extracts:
   - Page title
   - Meta description (or first 200 characters of text content)
   - All words on the page (filtered to alphabetic characters only)

3. **Graph Building**: As pages are crawled, the crawler builds a link graph:
   - Each URL is a node
   - Links between pages are edges
   - This graph is used for PageRank calculation

4. **Link Discovery**: The crawler parses all `<a>` tags and normalizes URLs:
   - Skips anchor links (`#`)
   - Converts protocol-relative URLs (`//example.com`)
   - Resolves relative URLs (`/path/to/page`)
   - Removes URL fragments

5. **PageRank Calculation**: After crawling completes, the `compute_pagerank()` function:
   - Implements the iterative PageRank algorithm
   - Uses a damping factor of 0.85 (default)
   - Handles dangling nodes (pages with no outgoing links)
   - Iterates until convergence or max iterations (100)
   - Returns importance scores for all discovered pages

6. **Rate Limiting**: Random delays (1-3 seconds) between requests help avoid overwhelming target servers

## Functions

### `index_page(webpage, webpage_url)`

Indexes a web page and extracts relevant information.

**Parameters:**
- `webpage`: BeautifulSoup object of the parsed HTML
- `webpage_url`: String URL of the page

**Returns:**
- Dictionary containing:
  - `url`: The page URL
  - `title`: Page title
  - `description`: Meta description or text preview
  - `words`: List of all words found on the page

### `compute_pagerank(graph, damping_factor=0.85, max_iterations=100, tol=1.0e-6)`

Computes PageRank scores for all URLs in the link graph using the iterative PageRank algorithm.

**Parameters:**
- `graph`: Dictionary mapping URLs to lists of outgoing links
- `damping_factor`: Probability of following a link (default: 0.85)
- `max_iterations`: Maximum number of iterations (default: 100)
- `tol`: Convergence tolerance (default: 1.0e-6)

**Returns:**
- Dictionary mapping each URL to its PageRank score

**Algorithm:**
- Initializes all pages with equal PageRank (1/N)
- Handles dangling nodes (pages with no outgoing links)
- Iteratively distributes PageRank through links
- Converges when total change is below tolerance

### `web_crawler()`

Main crawler function that discovers and processes web pages, builds the link graph, and computes PageRank.

**Returns:**
- Tuple containing:
  - `indexed_pages`: List of indexed page data
  - `graph`: Link graph dictionary
  - `pagerank_scores`: PageRank scores for all URLs

## Important Notes

⚠️ **Ethical Crawling**: 
- Always respect `robots.txt` files (not currently implemented)
- Be mindful of server load - consider increasing delays for production use
- Only crawl sites you have permission to crawl
- Consider implementing a maximum depth or page limit to avoid infinite crawling

⚠️ **Warning**: This crawler will continue indefinitely until manually stopped or it runs out of new URLs to visit. Consider adding:
- Maximum page limits
- Domain restrictions
- Depth limits
- Data persistence (currently indexed data is not saved)

## Future Improvements

- [ ] Save indexed data and PageRank scores to a database or file
- [ ] Respect `robots.txt`
- [ ] Add domain filtering to stay within specific sites
- [ ] Implement maximum crawl depth
- [ ] Add command-line arguments for configuration
- [ ] Multi-threading support for faster crawling
- [ ] Progress tracking and statistics
- [ ] Export PageRank results to CSV or JSON
- [ ] Visualize the link graph
- [ ] Implement personalized PageRank

## License

This project is provided as-is for educational purposes.
