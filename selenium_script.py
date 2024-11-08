#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome en modo sin cabecera
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Iniciar el servicio de ChromeDriver con ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Crear una instancia de WebDriver de Chrome con las opciones configuradas
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abrir la página web
url = "https://www.latamairlines.com/co/es/ofertas-vuelos?origin=BOG&inbound=2024-12-31T12%3A00%3A00.000Z&outbound=2024-12-23T12%3A00%3A00.000Z&destination=CTG&adt=1&chd=0&inf=0&trip=RT&cabin=Economy&redemption=false&sort=RECOMMENDED"
driver.get(url)

# Esperar a que el título de la página cargue como señal de que la página ha sido renderizada
try:
    WebDriverWait(driver, 10).until(EC.title_contains("LATAM"))
    print("Título de la página:", driver.title)
except Exception as e:
    print("No se pudo cargar el título:", e)

# Esperar a que los elementos de los vuelos estén presentes en el DOM
try:
    vuelos = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//ol[@aria-label="Vuelos disponibles."]/li[contains(@class, "bodyFlightsstyle__")]'))
    )
    print(f"Se encontraron {len(vuelos)} vuelos en la página.")
except Exception as e:
    print("No se encontraron elementos de vuelo:", e)
    driver.quit()
    exit()

# # Extraer información de cada vuelo
for i, vuelo in enumerate(vuelos):
    try:
        element = vuelo.find_element(By.XPATH, './/*[contains(@id, "FlightInfoComponent")]/div[1]/div[1]/span[1]')
        print(f"Vuelo {i + 1} - Hora de salida: {element.text}")
    except Exception as e:
        print(f"No se pudo obtener la información del vuelo {i + 1}: {e}")

# Cerrar el navegador al finalizar
driver.quit()
