import pytest
from unittest.mock import MagicMock
from tech_news.analyzer.reading_plan import ReadingPlanService


# dados de teste
mock_data = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "timestamp": "04/04/2021",
        "writer": "Eu",
        "reading_time": 4,
        "summary": "Algo muito bacana aconteceu",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "timestamp": "04/04/2021",
        "writer": "Eu",
        "reading_time": 4,
        "summary": "Algo muito bacana aconteceu",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "timestamp": "04/04/2021",
        "writer": "Eu",
        "reading_time": 13,
        "summary": "Algo muito bacana aconteceu",
        "category": "Ferramentas",
    },
]


def test_reading_plan_group_news():
    # Configura o mock para retornar os dados de teste
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_data)

    # Verifica se um valor inválido para `available_time` levanta ValueError
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-28)

    # Teste para verificar se os dados de teste são agrupados corretamente
    noticias = ReadingPlanService.group_news_for_available_time(12)
    print("🚀 ~ file: test_reading_plan.py:50 ~ news:", noticias)

    assert len(noticias["readable"]) == 1
    assert len(noticias["unreadable"]) == 1
    assert noticias["readable"][0]["unfilled_time"] == 4
