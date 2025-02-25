import psycopg2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

dados = [] 

try:
  
    url = "https://www.cnnbrasil.com.br/"
    driver.get(url)
    print(f"Acessando {url}...")

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//h3"))
    )

    noticias = driver.find_elements(By.XPATH, "//h3")

    for noticia in noticias[:5]:
        titulo = noticia.text.strip()

        try:
            link_elemento = noticia.find_element(By.XPATH, "./ancestor::a")
            link = link_elemento.get_attribute("href") if link_elemento else "Sem link"
        except:
            link = "Sem link"

        if titulo and link != "Sem link":
            dados.append((titulo, link))

    for titulo, link in dados:
        print(f"Título: {titulo}\nLink: {link}\n")

except Exception as e:
    print(f"Erro ao coletar dados do site: {e}")

finally:
    driver.quit()

conn = None
try:
    conn = psycopg2.connect(
        dbname="noticias_db",
        user="postgres",
        password="Cami1703@",
        host="localhost", 
        port="5432"
    )
    conn.set_client_encoding('UTF8')  
    cur = conn.cursor()

    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS noticias (
            id SERIAL PRIMARY KEY,
            titulo TEXT NOT NULL,
            link TEXT NOT NULL,
            data_extracao TIMESTAMP DEFAULT NOW()
        );
    """)

    for titulo, link in dados:
        cur.execute("INSERT INTO noticias (titulo, link) VALUES (%s, %s)", (titulo, link))

    conn.commit()
    print("Dados salvos no banco de dados com sucesso!")

except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

finally:
    if conn:
        cur.close()
        conn.close()