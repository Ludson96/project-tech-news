from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title: str):
    noticias = db.news.find(
        {"title": {"$regex": title, "$options": "i"}}
    ).limit(10)

    if noticias.count() == 0:
        return []

    tuple_news = [(noticia["title"], noticia["url"]) for noticia in noticias]
    return tuple_news


# Requisito 8
def search_by_date(date):
    try:
        data = datetime.strptime(date, "%Y-%m-%d")
        data_formatada = datetime.strftime(data, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    news = db.news.find(
        {"timestamp": {"$regex": data_formatada, "$options": "i"}}
    )

    if news.count() == 0:
        return []

    tuple_news = [(noticia["title"], noticia["url"]) for noticia in news]
    return tuple_news


# Requisito 9
def search_by_category(category):
    news = db.news.find(
        {"category": {"$regex": category, "$options": "i"}}
    ).limit(10)

    if news.count() == 0:
        return []

    tuple_news = [(noticia["title"], noticia["url"]) for noticia in news]
    return tuple_news
