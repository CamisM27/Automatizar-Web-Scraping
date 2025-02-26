FROM python:3.9-slim

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

COPY chromedriver.exe /usr/local/bin/chromedriver

RUN chmod +x /usr/local/bin/chromedriver

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/local/bin/chromedriver

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "scraper.py"]




