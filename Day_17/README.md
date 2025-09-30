# Day 17: Build Your Own Intelligent Internet Search Engine

## Project Overview

This project demonstrates the implementation of an intelligent web crawler using Crawl4AI, an open-source AI-powered web scraping framework. The assignment focuses on building a Breadth-First Search (BFS) web crawler capable of systematically exploring Wikipedia's link structure to a specified depth, showcasing modern web scraping techniques optimized for AI and data extraction workflows.

The implementation leverages asynchronous programming and advanced crawling strategies to efficiently navigate and extract data from large-scale websites while respecting domain boundaries and managing crawl depth.

## Assignment Requirements

The assignment challenge was to:

**"Can you run a BFS Crawl on Wikipedia?"**

**Specific Requirements:**
- Implement a BFS (Breadth-First Search) crawl on Wikipedia
- Use the crawl4ai library with `BFSDeepCrawlStrategy`
- Configure crawl parameters:
  - `max_depth=2` (crawl up to 2 levels deep)
  - `include_external=False` (stay within Wikipedia domain)
  - `max_pages=500` (limit total pages for practical execution time)
- Target URL: `https://www.wikipedia.org`
- Save crawl output to a text file
- Run locally (not compatible with Google Colab due to browser requirements)

## Technical Architecture

### Core Technologies

1. **Crawl4AI Framework**
   - Open-source AI web crawler
   - Optimized for LLM and AI agent workflows
   - Provides clean, structured Markdown output
   - 6x faster than conventional scraping methods

2. **Asynchronous Programming**
   - Python `asyncio` for concurrent operations
   - `AsyncWebCrawler` for non-blocking I/O
   - Efficient handling of multiple simultaneous requests

3. **BFS Crawling Strategy**
   - Breadth-First Search algorithm
   - Systematic exploration of link hierarchy
   - Depth-limited traversal
   - Domain-restricted crawling

4. **Browser Automation**
   - Playwright for browser control
   - JavaScript rendering support
   - Dynamic content handling

## Project Structure

```
Day_17/
├── 17_Build_Your_Own_Intelligent_Internet_Search_Engine.ipynb  # Tutorial notebook
├── Assignment_BFS_Web_Crawler.ipynb                            # Assignment implementation
├── run_and_save_output.py                                      # Standalone execution script
├── Output.txt                                                  # Crawl results (614 lines)
└── README.md                                                   # This file
```

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Windows, macOS, or Linux operating system
- Minimum 4GB RAM (8GB recommended)
- Internet connection for crawling

### Required Dependencies

```bash
pip install crawl4ai
playwright install
```

### Complete Installation Steps

1. **Install Crawl4AI:**
   ```bash
   pip install crawl4ai
   ```

2. **Install Playwright Browsers:**
   ```bash
   playwright install
   ```
   This downloads the necessary browser binaries (Chromium, Firefox, WebKit).

3. **Verify Installation:**
   ```bash
   python -c "import crawl4ai; print('Crawl4AI installed successfully')"
   ```

## Usage Instructions

### Method 1: Running the Standalone Script

Execute the Python script directly:

```bash
cd Day_17
python run_and_save_output.py
```

This will:
- Start the BFS crawler on Wikipedia
- Display real-time progress in the console
- Save all output to `Output.txt`
- Show summary statistics upon completion

### Method 2: Running in Jupyter Notebook

1. Open the assignment notebook:
   ```bash
   jupyter notebook Assignment_BFS_Web_Crawler.ipynb
   ```

2. Execute all cells sequentially

3. Output will be displayed inline and saved to `Output.txt`

### Method 3: Using the Core Code

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

async def main():
    # Configure BFS crawl
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=2,
            max_pages=500,
            include_external=False
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True
    )
    
    # Execute crawl
    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun("https://www.wikipedia.org", config=config)
        
        print(f"Crawled {len(results)} pages in total")
        
        # Process results
        for result in results[:3]:
            print(f"URL: {result.url}")
            print(f"Depth: {result.metadata.get('depth', 0)}")
            print(f"Title: {result.metadata.get('title', 'N/A')}")

# Run the crawler
asyncio.run(main())
```

## Implementation Details

### BFS Crawling Strategy

The Breadth-First Search strategy explores web pages level by level:

1. **Level 0 (Depth 0):** Start page (`https://www.wikipedia.org`)
2. **Level 1 (Depth 1):** All pages linked from the start page
3. **Level 2 (Depth 2):** All pages linked from Level 1 pages

**Configuration Parameters:**

```python
BFSDeepCrawlStrategy(
    max_depth=2,           # Maximum crawl depth
    max_pages=500,         # Maximum total pages to crawl
    include_external=False # Only crawl internal Wikipedia links
)
```

### Output Redirection

The implementation uses a custom `TeeOutput` class to simultaneously:
- Display output in the console
- Write output to `Output.txt`
- Capture output for notebook integration

```python
class TeeOutput:
    def __init__(self, *files):
        self.files = files
    
    def write(self, data):
        for f in self.files:
            f.write(data)
            f.flush()
    
    def flush(self):
        for f in self.files:
            f.flush()
```

### Crawl Progress Tracking

The crawler provides real-time feedback for each page:

```
[FETCH]... ↓ https://ab.wikipedia.org    | ✓ | ⏱: 1.09s
[SCRAPE].. ◆ https://ab.wikipedia.org    | ✓ | ⏱: 0.25s
[COMPLETE] ● https://ab.wikipedia.org    | ✓ | ⏱: 1.35s
```

- **FETCH:** Downloading the page
- **SCRAPE:** Extracting content
- **COMPLETE:** Processing finished

## Crawl Results

### Execution Summary

Based on the `Output.txt` file:

- **Total Pages Crawled:** Multiple Wikipedia language editions
- **Crawl Strategy:** BFS (Breadth-First Search)
- **Maximum Depth:** 2 levels
- **Page Limit:** 500 pages
- **Domain Restriction:** Wikipedia only (no external links)

### Sample Crawled Pages

The crawler successfully visited various Wikipedia language editions:
- `https://www.wikipedia.org` (main page)
- `https://ab.wikipedia.org` (Abkhazian)
- `https://ace.wikipedia.org` (Acehnese)
- `https://ady.wikipedia.org` (Adyghe)
- `https://af.wikipedia.org` (Afrikaans)
- And many more language editions...

### Performance Metrics

Average timing per page:
- **Fetch Time:** 0.9 - 2.5 seconds
- **Scrape Time:** 0.2 - 0.5 seconds
- **Total Time:** 1.0 - 3.0 seconds per page

## Key Features

1. **Asynchronous Execution**
   - Non-blocking I/O operations
   - Concurrent page processing
   - Efficient resource utilization

2. **Depth-Limited Crawling**
   - Prevents infinite crawling loops
   - Controls scope of data collection
   - Manages execution time

3. **Domain Restriction**
   - Stays within Wikipedia domain
   - Respects site boundaries
   - Avoids external link following

4. **Real-Time Progress Monitoring**
   - Live status updates
   - Timing information per page
   - Success/failure indicators

5. **Persistent Output**
   - Saves results to text file
   - Preserves crawl history
   - Enables post-processing analysis

## Crawl4AI Advantages

### Optimized for AI Workflows
- Generates clean Markdown output
- Structured data extraction
- Ready for RAG (Retrieval-Augmented Generation)
- Suitable for model fine-tuning

### High Performance
- 6x faster than traditional methods
- Advanced heuristic algorithms
- Reduced API call costs
- Efficient data acquisition

### Flexible Browser Control
- Session management
- Proxy integration
- Custom hooks
- Reliable data access

### Open Source and Deployable
- No API keys required
- Docker-ready
- Cloud or on-premise deployment
- Active community support

## Limitations and Considerations

1. **Browser Requirements**
   - Requires Playwright browser installation
   - Not compatible with Google Colab
   - Needs local execution environment

2. **Resource Consumption**
   - Memory usage increases with page count
   - CPU intensive during scraping
   - Network bandwidth dependent

3. **Crawl Time**
   - Large crawls can take significant time
   - 500 pages may take 10-30 minutes
   - Depends on network speed and site responsiveness

4. **Rate Limiting**
   - Should respect robots.txt
   - May need delays between requests
   - Risk of IP blocking with aggressive crawling

## Best Practices

1. **Respect Website Policies**
   - Check robots.txt before crawling
   - Implement appropriate delays
   - Limit concurrent requests

2. **Manage Crawl Scope**
   - Set reasonable max_depth values
   - Use max_pages to limit execution time
   - Filter by domain when appropriate

3. **Error Handling**
   - Implement retry logic for failed requests
   - Log errors for debugging
   - Handle timeouts gracefully

4. **Resource Management**
   - Monitor memory usage
   - Close browser sessions properly
   - Clean up temporary files

## Assignment Completion Status

**Status:** FULLY COMPLETED

All requirements have been successfully implemented:
- BFS crawl on Wikipedia: Complete
- crawl4ai library usage: Implemented
- BFSDeepCrawlStrategy: Configured correctly
- max_depth=2: Set as required
- include_external=False: Configured
- max_pages=500: Implemented for practical execution
- Output saved to text file: Output.txt created
- Local execution: Verified (not Colab)

## Future Enhancements

Potential improvements for the crawler:
- Implement distributed crawling for scalability
- Add content filtering and extraction rules
- Integrate with vector databases for semantic search
- Implement incremental crawling for updates
- Add support for authentication and cookies
- Create visualization of crawl graph structure
- Implement parallel crawling with multiple workers

## References and Resources

- **Crawl4AI Documentation:** https://crawl4ai.com/
- **Crawl4AI GitHub:** https://github.com/unclecode/crawl4ai
- **Playwright Documentation:** https://playwright.dev/python/
- **Python asyncio:** https://docs.python.org/3/library/asyncio.html
- **BFS Algorithm:** https://en.wikipedia.org/wiki/Breadth-first_search

## Troubleshooting

### Common Issues

**Issue:** `crawl4ai not installed` error
```bash
Solution: pip install crawl4ai
```

**Issue:** `playwright not found` error
```bash
Solution: playwright install
```

**Issue:** Browser fails to launch
```bash
Solution: Ensure Playwright browsers are installed
playwright install chromium
```

**Issue:** Memory errors with large crawls
```bash
Solution: Reduce max_pages parameter or increase system RAM
```

## License

This project is part of an educational assignment and uses open-source libraries under their respective licenses.


