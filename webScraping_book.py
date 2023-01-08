from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import re

from bs4 import BeautifulSoup


class webScraping_book():

     # La siguiente función hereda la clase para manejar el navegador, observa que instalas el driver en la RAM
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self._driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install())) # Inicias el navegador
        self._url = url
    
     # En el siguiente método cargas la página web
    def cargar_page(self):
        driver = self._driver # No es necesario hacer esto, pero te resume código
        url_market = str(self._url) # Así no te presenta problemas para colocar el string
        driver.implicitly_wait(10) # Esperas 10 segundos (mientras carga el navegador)
        driver.maximize_window() # Maximizas la ventana del navegador 
        driver.get(url_market) # Vas a la página web que deseas

    
    def obtain_results(self):
        try:
            # Esperas 3 segundos hasta que el texto de resultados esté habilitado
           WebDriverWait(self._driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="default"]/div/div/div/div/form/strong[1]'))) 
            
        except:
            # En caso de no cargar el texto, cierras el navegador
            print("No se encontró el elemento")
            self._driver.close()
        
        # En caso de cargar el navegador, lo llevas a una variable y luego le envías el producto a buscar
        result= self._driver.find_element(By.XPATH, '//*[@id="default"]/div/div/div/div/form/strong[1]')
        numResult = result.get_attribute('strong')
        print(numResult)
    

if __name__ == "__main__":

    # Estos son los parámetros que has configurado para la página por el momento
    url = 'http://books.toscrape.com/'
    library = webScraping_book(url)
    library.cargar_page()
    library.obtain_results()
