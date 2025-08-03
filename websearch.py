import requests
from bs4 import BeautifulSoup
from ddgs import DDGS
from typing import List, Dict
import time


def web_search(query: str, num_results: int = 5) -> List[Dict[str, str]]:
    """
    Performs a web search using DuckDuckGo and returns cleaned content from the websites.
    
    Args:
        query (str): The search query
        num_results (int): Number of search results to return (default: 5)
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries containing 'url' and 'content' keys
    """
    results = []
    
    try:
        # Initialize DuckDuckGo search
        with DDGS() as ddgs:
            # Get search results
            search_results = list(ddgs.text(query, max_results=num_results))
            
            print(f"Found {len(search_results)} search results for: '{query}'")
            
            # Process each search result
            for i, result in enumerate(search_results, 1):
                url = result.get('href', '')
                title = result.get('title', '')
                
                print(f"Processing {i}/{len(search_results)}: {title}")
                
                # Get and clean content from the URL
                content = get_cleaned_content(url)
                
                if content:
                    results.append({
                        'url': url,
                        'title': title,
                        'content': content
                    })
                else:
                    print(f"  Failed to retrieve content from: {url}")
                
                # Add a small delay to be respectful to websites
                time.sleep(1)
                
    except Exception as e:
        print(f"Error during search: {str(e)}")
    
    return results


def get_cleaned_content(url: str) -> str:
    """
    Retrieves and cleans content from a given URL using BeautifulSoup.
    
    Args:
        url (str): The URL to fetch content from
    
    Returns:
        str: Cleaned text content from the webpage
    """
    try:
        # Set headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make request with timeout
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "header", "footer", "aside"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up the text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Limit content length (optional - adjust as needed)
        if len(text) > 5000:
            text = text[:5000] + "..."
        
        return text
        
    except requests.exceptions.RequestException as e:
        print(f"  Request error for {url}: {str(e)}")
        return ""
    except Exception as e:
        print(f"  Error processing {url}: {str(e)}")
        return ""


# Example usage
if __name__ == "__main__":
    """ # Test the function
    query = "Python web scraping tutorials"
    num_results = 3
    
    print(f"Searching for: '{query}'")
    print(f"Number of results: {num_results}")
    print("-" * 50)
    
    results = web_search(query, num_results)
    
    print(f"\nFound {len(results)} results with content:")
    print("=" * 50)
    
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Content (first 200 chars): {result['content'][:200]}...")
        print("-" * 50) """
