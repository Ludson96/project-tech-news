import requests
import time
from parsel import Selector

HTML = str


# Requisito 1
def fetch(url: str) -> HTML | None:
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
    except requests.exceptions.Timeout:
        return None

    time.sleep(1)

    if response.status_code == 200:
        return response.text

    return None


# Requisito 2
def scrape_updates(html_content: HTML) -> list:
    try:
        selector = Selector(text=html_content)
        all_links = selector.css(".cs-overlay a::attr(href)").getall()
    except ValueError as e:
        print(f"Erro ao tentar obter links: {e}")
        return []
    else:
        return all_links


# Requisito 3
def scrape_next_page_link(html_content: HTML) -> None | str:
    try:
        selector = Selector(text=html_content)
        link_next_page = selector.css(".next.page-numbers::attr(href)").get()
    except ValueError:
        return None
    else:
        return link_next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    summary_content = selector.css(
        "div.entry-content > p:first-of-type *::text"
    ).getall()
    summary = "".join(summary_content).strip()

    info_noticias = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".url.fn.n::text").get(),
        "reading_time": int(
            selector.css(".meta-reading-time::text").re_first(r"\d+")
        ),
        "summary": summary,
        "category": selector.css(".label::text").get(),
    }
    return info_noticias


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
