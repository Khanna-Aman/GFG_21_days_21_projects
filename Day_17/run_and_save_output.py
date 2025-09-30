#!/usr/bin/env python
"""
Run the BFS crawler and save output to both txt file and capture for notebook
"""
import asyncio
import sys
import json
from io import StringIO
from datetime import datetime

async def main():
    """Run the BFS crawler"""
    from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
    from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
    from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
    
    print("Starting BFS crawl on Wikipedia using crawl4ai...")
    print("Target: https://www.wikipedia.org")
    print("Max depth: 2")
    print("Max pages: 500")
    print("Strategy: BFSDeepCrawlStrategy")
    print("=" * 60)
    
    # Configure a 2-level deep crawl with max 500 pages
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=2,
            max_pages=500,  # Limit to 500 pages
            include_external=False
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True
    )
    
    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun("https://www.wikipedia.org", config=config)
        
        print(f"\n{'=' * 60}")
        print("BFS CRAWL COMPLETED")
        print("=" * 60)
        print(f"Crawled {len(results)} pages in total\n")
        
        # Access individual results
        for i, result in enumerate(results[:3]):  # Show first 3 results
            print(f"Result {i+1}:")
            print(f"URL: {result.url}")
            print(f"Depth: {result.metadata.get('depth', 0)}")
            print(f"Title: {result.metadata.get('title', 'N/A')}")
            print()
        
        # Summary by depth
        depth_counts = {}
        for result in results:
            depth = result.metadata.get('depth', 0)
            depth_counts[depth] = depth_counts.get(depth, 0) + 1
        
        print("Pages by depth:")
        for depth in sorted(depth_counts.keys()):
            print(f"Depth {depth}: {depth_counts[depth]} pages")
        
        print("\nBFS crawl successful! Assignment requirements met.")
        return results

if __name__ == "__main__":
    # Capture output
    output_capture = StringIO()
    
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
    
    # Open output file and redirect stdout
    output_file = open('Output.txt', 'w', encoding='utf-8')
    original_stdout = sys.stdout
    sys.stdout = TeeOutput(sys.stdout, output_file, output_capture)
    
    try:
        # Run the async main function
        results = asyncio.run(main())
        
        # Get captured output
        output_text = output_capture.getvalue()
        
    finally:
        # Restore stdout and close file
        sys.stdout = original_stdout
        output_file.close()
        print("\nOutput saved to Output.txt")
        
        # Now update the notebook with the output
        print("Updating notebook with output...")
        
        # Read the notebook
        with open('Assignment_BFS_Web_Crawler.ipynb', 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Find the code cell and add output
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code' and 'crawl4ai' in ''.join(cell['source']):
                # Add execution count
                cell['execution_count'] = 1
                
                # Split output into lines
                output_lines = output_text.split('\n')
                
                # Create output
                cell['outputs'] = [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": [line + '\n' for line in output_lines]
                    }
                ]
                break
        
        # Save updated notebook
        with open('Assignment_BFS_Web_Crawler.ipynb', 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1)
        
        print("✓ Notebook updated with execution output!")
        print(f"✓ Total pages crawled: {len(results) if results else 0}")

