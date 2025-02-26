# Automação de Web Scraping com Selenium e PostgreSQL em Docker

Este projeto realiza Web Scraping no site da CNN Brasil para coletar títulos e links das notícias e armazená-los em um banco de dados PostgreSQL, utilizando Selenium para automação do navegador e Docker para containerização. O projeto permite a extração automatizada de informações, facilitando a análise e o armazenamento dos dados coletados.

# Tecnologias Utilizadas

-Python → Linguagem da programação
-Selenium → Automação de navegadores
-PostgreSQL → Banco de dados
-Docker → Containerização de aplicações
-Docker Compose → Gerenciamento de containers
-Chromedriver → Webdriver

# Estrutura do projeto

-scraper.py → Script Python que coleta os dados.
-schema.sql → Script SQL para criar a tabela notícias.
-Dockerfile → Define o ambiente do scraper.
-docker-compose.yml → Configura os serviços do Docker.
-README.md → Este arquivo contendo as instruções de uso.
-Chromedriver: Necessário para o Selenium controlar o navegador.
-requirements.txt: Contém todas as bibliotecas Python necessárias.

# Funcionamento

Primeiramente, o script faz com que o Selenium abra o navegador e acesse a página web. Em seguida, ele extrai os cinco primeiros títulos e links das notícias encontradas na página. Após a extração, os dados são inseridos no banco de dados PostgreSQL, garantindo que fiquem armazenados para futuras consultas.
O projeto é executado dentro de containers Docker, o que facilita a configuração e a reprodução do ambiente em qualquer máquina.

# Instalação e Configuração

Dentro do CMD(Prompt de Comando), clone este repositório com o comando: git clone https://github.com/CamisM27/Automatizar-Web-Scraping, navegue até a pasta do projeto, verifique se você possui as dependências necessárias para rodar o projeto e suba os containers utilizando Docker Compose: docker-compose up --build

# Como Usar
O script de web scraping será executado automaticamente ao iniciar o container Docker, para isso, acesse o CMD (Prompt de Comando) e execute: docker start meu_postgres 
Para acessar o banco de dados e verificar os dados armazenados insira o comando: docker exec -it meu_postgres psql -U postgres -d noticias_db. Depois, insira: SELECT * FROM noticias;