import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(html_content)

    news_dict = {
        "url": selector.css("link[rel*=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()) or 0,
        "summary": selector.xpath("string(//p)").get().strip(),
        "tags": selector.css("section.post-tags a::text").getall(),
        "category": selector.css("div.entry-details span.label::text").get(),
    }
    return news_dict


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    page = 0
    news_list = []

    while page < amount:
        html = fetch(url)
        news_page = scrape_novidades(html)
        for news in news_page:
            if page == amount:
                break
            new = scrape_noticia(fetch(news))
            news_list.append(new)
            page += 1
        url = scrape_next_page_link(html)

    create_news(news_list)
    return news_list
