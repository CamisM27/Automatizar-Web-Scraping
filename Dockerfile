FROM python:3.9-slim

# Instalar dependências do sistema necessárias para o Selenium e o Chromium
RUN apt-get update && \
    apt-get install -y \
    chromium \
    wget \
    curl \
    unzip \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libx11-xcb1 \
    libxtst6 \
    libnss3 \
    libxrandr2 \
    libgbm1 \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Copiar o ChromeDriver da máquina local para o contêiner
COPY chromedriver.exe /usr/local/bin/chromedriver

# Dar permissão de execução ao ChromeDriver
RUN chmod +x /usr/local/bin/chromedriver

# Definir variáveis de ambiente para o Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/local/bin/chromedriver

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . /app/

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o script Python
CMD ["python", "scraper.py"]




