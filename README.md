# Repositório do projeto Tech News 🗞️

## Módulo: CIÊNCIA DA COMPUTAÇÃO

 Repositório possuí projeto desenvolvido no período que estive na **Trybe**, abordando conceitos de `POO`, `Raspagem de dados` e `banco de dados`.

## Informações de aprendizados

- Este é um projeto desenvolvido para praticar `Python`;
- Primeiro projeto usando `MongoDB` com `Python`;
- Utilizei o `Pytest` para fazer meus testes;
- Utilizei os módulos `request` e `parsel` para fazer raspagem e `pymongo` para usar mongodb com python.

## Linguagens e ferramentas usadas

[![Git][Git-logo]][Git-url]
[![Python][Python-logo]][Python-url]
[![Pytest][Pytest-logo]][Pytest-url]
[![Mongo][Mongo-logo]][Mongo-url]

## O que foi desenvolvido

Este projeto, tem como principal objetivo fazer consultas em notícias sobre tecnologia.

As notícias foram obtidas através da raspagem do [blog da Trybe](https://blog.betrybe.com/).

## Habilidades trabalhadas

- Utilizar o terminal interativo do Python
- Escrever seus próprios módulos e importá-los em outros códigos
- Aplicar técnicas de raspagem de dados
- Extrair dados de conteúdo HTML
- Armazenar os dados obtidos em um banco de dados

## Instruções para instalar e rodar

<details>

1. Clone o repo:

    ```bash-shell
    git clone git@github.com:Ludson96/project-tech-news.git
    ```

1. Entre na pasta do repositório que você acabou de clonar:

    ```bash-shell
    cd project-tech-news
    ```

1. Caso não tenha instalado o python, pode usar o docker:

    ```bash
    docker build -t nome-da-imagem

    docker run -it nome-da-imagem
    ```

1. Caso não tenha instalado o MongoDB, pode usar o docker-compose:

    ```bash
    docker-compose up -d 
    ```

1. Crie e ative o ambiente virtual:

    ```bash-shell
    python3 -m venv .venv && source .venv/bin/activate
    ```

1. Instale as dependências no ambiente virtual:

    ```bash
    python3 -m pip install -r dev-requirements.txt
    ```

1. Para rodar todos os testes utilize o comando:

    ```bash
    python3 -m pytest
    ```

1. Para rodar apenas em um arquivo:

    ```bash-shell
    python3 -m pytest <path do arquivo>
    ```

1. Para executar a classe principal execute o comando abaixo:

     ```bash-shell
    tech-news-analyzer

    #siga os passos no terminal
    ```
    
    </details>

## Raspagem

Abaixo está uma lista das funções de raspagem disponíveis no arquivo `scraper.py`.

<details>

### `fetch(url)`

Essa função recebe uma URL como parâmetro, realiza uma solicitação GET na URL e retorna o conteúdo HTML da página.

Exemplo de uso:

```python
html_content = fetch("https://www.example.com")
```

### `scrape_updates(html_content)`

Essa função recebe o conteúdo HTML da página como parâmetro e retorna uma lista de links para as atualizações de notícias no site.

Exemplo de uso:

```python
news_links = scrape_updates(html_content)
```

### `scrape_next_page_link(html_content)`

Essa função recebe o conteúdo HTML da página como parâmetro e retorna o link para a próxima página de atualizações.

Exemplo de uso:

```python
next_page_link = scrape_next_page_link(html_content)
```

### `scrape_news(html_content)`

Essa função recebe o conteúdo HTML da página como parâmetro e retorna um dicionário com informações sobre uma notícia específica.

Exemplo de uso:

```python
news_info = scrape_news(html_content)
```

### `get_tech_news(n)`

Essa função recebe um número inteiro n como parâmetro e retorna uma lista com as últimas n notícias do site.

Exemplo de uso:

```python
latest_news = get_tech_news(10)
```

</details>

> `docker-compose.yml` fornecido pela trybe.

[Git-logo]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com
[Python-logo]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Pytest-logo]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/en/7.2.x/
[Mongo-url]:https://www.mongodb.com/
[Mongo-logo]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white
