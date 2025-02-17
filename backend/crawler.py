import requests
from bs4 import BeautifulSoup
import json

def crawl_sitemap(sitemap_url):
    """
    Crawl a sitemap to get the list of URLs.
    :param sitemap_url: URL of the sitemap.xml
    :return: list of URLs
    """
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, "xml")
    urls = [loc.text for loc in soup.find_all("loc")]
    return urls

def crawl_page(url):
    """
    Crawl a webpage and extract content.
    :param url: URL of the page
    :return: dictionary with title and content of the page
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else 'No Title'
    content = soup.get_text()
    return {'url': url, 'title': title, 'content': content}

def crawl_website(sitemap_url):
    urls = crawl_sitemap(sitemap_url)
    pages = []
    for url in urls:
        page = crawl_page(url)
        pages.append(page)
    return pages

if __name__ == "__main__":
    sitemap_url = "https://www.semrush.com/blog/xml-sitemap/"   
    website_data = crawl_website(sitemap_url)
    with open("website_data.json", "w") as f:
        json.dump(website_data, f)
