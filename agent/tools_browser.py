from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup
import os

# Get API key from environment variable
SERPAPI_KEY = os.environ.get("SERPAPI_API_KEY")

def serpapi_search(query, num_results=3):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num_results,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    links = []
    if "organic_results" in results:
        for result in results["organic_results"][:num_results]:
            link = result.get("link")
            if link:
                links.append(link)
    return links

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text() for p in paragraphs[:4]])
        return text
    except Exception as e:
        return f"[Error scraping {url}: {e}]"
