# Automação de Web Scraping com Selenium e PostgreSQL em Docker

Este projeto realiza Web Scraping no site da CNN Brasil para coletar títulos e links das notícias e armazená-los em um banco de dados PostgreSQL, utilizando Selenium para automação do navegador e Docker para containerização, usando docker-compose.

# Tecnologias Utilizadas


# Estrutura do projeto

-scraper.py → Script Python que coleta os dados.
-schema.sql → Script SQL para criar a tabela notícias.
-Dockerfile → Define o ambiente do scraper.
-docker-compose.yml → Configura os serviços do Docker.
-README.md → Este arquivo contendo as instruções de uso.
-Chromedriver: Necessário para o Selenium controlar o navegador.
-requirements.txt: Contém todas as bibliotecas Python necessárias.