import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, {"user-agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
        return response.text
    except BaseException:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    list = selector.css(".cs-overlay-link::attr(href)").getall()
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        selector = Selector(html_content)
        next = selector.css(".next::attr(href)").get()
    except (next == ""):
        return None
    return next


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
