from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(item["title"], item["url"]) for item in news]


# Requisito 7
def search_by_date(date):
    try:
        date_time = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news = search_news({"timestamp": date_time})
        return [(item["title"], item["url"]) for item in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = search_news(
        {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}})
    return [(item["title"], item["url"]) for item in news]


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(item["title"], item["url"]) for item in news]
