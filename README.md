# Web Crawler

A Python-based web crawler that recursively discovers and indexes web pages starting from a seed URL.

## Features

- **Recursive crawling**: Automatically discovers and follows links from web pages
- **Page indexing**: Extracts and stores title, description, and word content from each page
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

By default, the crawler starts at `https://www.wikipedia.org/` and will continue crawling links it discovers.

### Customizing the Starting URL

Edit the `urls` list in the `web_crawler()` function:

```python
urls = ["https://your-starting-url.com/"]
```

## How It Works

1. **Crawling**: The crawler maintains a queue of URLs to visit and a set of already-visited URLs to avoid duplicates

2. **Indexing**: For each page visited, the `index_page()` function extracts:
   - Page title
   - Meta description (or first 200 characters of text content)
   - All words on the page (filtered to alphabetic characters only)

3. **Link Discovery**: The crawler parses all `<a>` tags and normalizes URLs:
   - Skips anchor links (`#`)
   - Converts protocol-relative URLs (`//example.com`)
   - Resolves relative URLs (`/path/to/page`)
   - Removes URL fragments

4. **Rate Limiting**: Random delays (1-3 seconds) between requests help avoid overwhelming target servers

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

### `web_crawler()`

Main crawler function that discovers and processes web pages.

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

- [ ] Save indexed data to a database or file
- [ ] Respect `robots.txt`
- [ ] Add domain filtering to stay within specific sites
- [ ] Implement maximum crawl depth
- [ ] Add command-line arguments for configuration
- [ ] Multi-threading support for faster crawling
- [ ] Progress tracking and statistics

## License

This project is provided as-is for educational purposes.
