from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories
import sys


def analyzer_menu():
    option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
 """
    )

    opcoes = {
        "0": "Digite quantas notícias serão buscadas: ",
        "1": "Digite o título: ",
        "2": "Digite a data no formato aaaa-mm-dd: ",
        "3": "Digite a categoria: ",
    }

    funcoes = {
        "0": get_tech_news,
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_category,
    }

    if option in opcoes:
        parametro = input(opcoes[option])
        print(funcoes[option](parametro))
    elif option == "4":
        print(top_5_categories())
    elif option == "5":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)
