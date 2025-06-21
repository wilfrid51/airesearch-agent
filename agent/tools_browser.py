from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Try to import SerpAPI, but make it optional
try:
    from serpapi import GoogleSearch
    SERPAPI_AVAILABLE = True
except ImportError:
    SERPAPI_AVAILABLE = False

def serpapi_search(query, num_results=3):
    # If SerpAPI is not available or no API key, fallback to regular search
    if not SERPAPI_AVAILABLE or not os.getenv("SERPAPI_KEY"):
        return google_search(query, num_results)
    
    try:
        params = {
            "engine": "google",
            "q": query,
            "api_key": os.getenv("SERPAPI_KEY"),
            "num": num_results
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        links = []
        if "organic_results" in results:
            for result in results["organic_results"][:num_results]:
                links.append(result.get("link"))
        return links
    except Exception as e:
        print(f"SerpAPI search failed: {e}")
        return google_search(query, num_results)

def google_search(query, num_results=3):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    links = []
    results = driver.find_elements(By.CSS_SELECTOR, 'a')
    for r in results:
        href = r.get_attribute('href')
        if href and "http" in href and "google.com" not in href:
            links.append(href)
        if len(links) >= num_results:
            break
    driver.quit()
    return links

def scrape_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    paragraphs = soup.find_all('p')
    text = "\n".join([p.get_text() for p in paragraphs[:4]])
    driver.quit()
    return text
