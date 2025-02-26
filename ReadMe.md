# Automação de Web Scraping com Selenium e PostgreSQL em Docker

Este projeto realiza Web Scraping no site da CNN Brasil para coletar títulos e links das notícias e armazená-los em um banco de dados PostgreSQL, utilizando Selenium para automação do navegador e Docker para containerização, usando docker-compose. O projeto permite a extração automatizada de informações, facilitando a análise e o armazenamento dos dados coletados.

# Tecnologias Utilizadas

-Python → Linguagem da programação
-Selenium → Automação de navegadores
-PostgreSQL → Banco de dados
-Docker → Containerização de aplicações
-Docker Compose →
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

O projeto utiliza Selenium para coletar dados da CNN Brasil e armazená-los em um banco de dados PostgreSQL, tudo rodando dentro de containers Docker.
O script funciona da seguinte maneira: primeiro, o Selenium abre o navegador e acessa a página web. Em seguida, ele extrai os cinco primeiros títulos e links das notícias encontradas na página. Após a extração, os dados são inseridos no banco de dados PostgreSQL, garantindo que fiquem armazenados para futuras consultas.
O projeto é executado dentro de containers Docker, o que facilita a configuração e a reprodução do ambiente em qualquer máquina.