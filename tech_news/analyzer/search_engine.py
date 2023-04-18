from tech_news.database import db


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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
