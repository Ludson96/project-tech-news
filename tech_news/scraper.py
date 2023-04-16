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
def scrape_next_page_link(html_content):
    "Seu código deve vir aqui"


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
