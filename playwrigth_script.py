#!/usr/bin/env python3

from playwright.sync_api import sync_playwright

url = "https://www.latamairlines.com/co/es/ofertas-vuelos?origin=BOG&inbound=2024-12-31T12%3A00%3A00.000Z&outbound=2024-12-23T12%3A00%3A00.000Z&destination=CTG&adt=1&chd=0&inf=0&trip=RT&cabin=Economy&redemption=false&sort=RECOMMENDED"

with sync_playwright() as p:
    # Inicia el navegador en modo headless
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Abre la página de LATAM
    page.goto(url)
    
    # Espera a que los elementos de los vuelos estén en la página
    page.wait_for_selector('li[class^="bodyFlightsstyle__"]')
    
    # Selecciona todos los elementos de vuelos
    vuelos = page.query_selector_all('li[class^="bodyFlightsstyle__"]')
    
    # Extraer información de cada vuelo
    for i, vuelo in enumerate(vuelos):
        try:
            # Busca la hora de salida del vuelo
            hora_salida = vuelo.query_selector('div[data-testid="flight-info-0-origin"] span.TextHourFlight')
            if hora_salida:
                print(f"Vuelo {i + 1} - Hora de salida: {hora_salida.inner_text()}")
            else:
                print(f"Vuelo {i + 1} - Hora de salida no encontrada.")
        except Exception as e:
            print(f"No se pudo obtener la información del vuelo {i + 1}: {e}")
    
    # Cierra el navegador al finalizar
    browser.close()
