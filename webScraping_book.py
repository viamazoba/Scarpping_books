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

        # Las listas siguientes serviran para alamacenar la información de los libros
        self._titles = []
        self._prices = []
        self._stars = []
        self._states = []
        self._description = []
    
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
        # retornas la cantidad de resultados de la página
        return result.text

    def obtain_genres(self):
        # Se obtiene la etiqueta '<ul>' con todos los géneros
        genres = self._driver.find_element(By.XPATH, '//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul')
        # Se obtienen todos los elementos <li> de la etiqueta '<ul>'
        genres_tags = genres.find_elements(By.TAG_NAME,'li')
        # Obtienes todos los elementos '<a>'
        genres_ref = genres.find_elements(By.TAG_NAME, 'a')
        # Obtienes el atributo 'href' de las etiquetas '<a>' para ir a los diferentes géneros
        genres_ref_list = [i.get_attribute("href") for i in genres_ref]
        # Se obtiene el texto de las etiquetas
        genres_list = [element.text for element in genres_tags]
        return genres_list,genres_ref_list
    
    def click_selected_genre(self):
        # Aquí vas a tomar la referencia del género seleccionado
        x = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
        #element = self._driver.find_element(By.XPATH, "//a[@href='{}']".format(x))
        #element.click()
        
        # Aquí abres una nueva ventana con la referencia que obtuviste
        self._driver.execute_script("window.open('{}');".format(x))
        # Obtienes las pestañas abiertas
        tabs = self._driver.window_handles
        # Seleccionas la nueva ventana abierta para trabajar
        self._driver.switch_to.window(tabs[-1])

    
     
    """El método a continuación obtiene la descripción del libro al entregarle la dirección a su HTML"""
    def book_description(self, url):

        # Aquí abres una nueva ventana con la referencia que obtuviste
        self._driver.execute_script("window.open('{}');".format(url))
        # Obtienes las pestañas abiertas
        tabs = self._driver.window_handles
        # Seleccionas la nueva ventana abierta para trabajar
        self._driver.switch_to.window(tabs[-1])

        product = self._driver.find_elements(By.TAG_NAME, 'article')
        tag_description = product[0].find_element(By.XPATH, '//*[@id="content_inner"]/article/p')
        description = tag_description.text
        print(description) 

        # Se cierra la ventana
        self._driver.close()
        # Regresamos a la ventana anterior (ventana principal)
        self._driver.switch_to.window(self._driver.window_handles[0])



        return description 

    
    def obtain_info_books(self):
        # Se obtienen todos los artículos visibles en la página
        articles = self._driver.find_elements(By.TAG_NAME, 'article')


        # Las siguientes líneas hasta el print las puedes borrar si no vas hacer más pruebas
        tag_star = articles[0].find_element(By.CLASS_NAME, 'star-rating')
        #title = tag_principal_title.find_element(By.TAG_NAME, 'a')
        print(tag_star.get_attribute('class').split(' ')[1])
        

        for book in articles:
            # A continuación se debe buscar dentro de las etiquetas h3 las etiquetas a
            # las cuales tienen en un atributo el título completo de los libros
            tag_principal_title = book.find_element(By.TAG_NAME, 'h3')
            title = tag_principal_title.find_element(By.TAG_NAME, 'a')

            # Se toma la dirección del HTML del libro, esto para obtener la descripción del mismo
            html_book = title.get_attribute('href')
            self._description.append(self.book_description(html_book))
            # A continuación se hace algo similar para obtener el rating de los libros
            tag_star = book.find_element(By.CLASS_NAME, 'star-rating')

            self._titles.append(title.get_attribute('title'))
            self._prices.append(book.text.split('\n')[1])
            self._stars.append(tag_star.get_attribute('class').split(' ')[1])
            self._states.append(book.text.split('\n')[2]) 

    
    """En el siguiente método se le da click() a next para pasar a la siguiente página"""
    def next_page(self):

        elements = self._driver.find_elements(By.CLASS_NAME, 'next')
        # Se establece una condición por si no existe el elemento next (última página)
        if elements:
            next_button = elements[0].find_element(By.TAG_NAME, 'a')
            next_button.click()

    """Cierras el browser"""
    def close_web(self):
        # Se cierra la ventana
        self._driver.close()

   

if __name__ == "__main__":

    # Estos son los parámetros que has configurado para la página por el momento
    url = 'http://books.toscrape.com/'
    library = webScraping_book(url)
    library.cargar_page()
    print('resultados :',library.obtain_results())
    #print(library.obtain_genres())
    generos , referencias = library.obtain_genres()
    #print(referencias)
    library.obtain_info_books()
    library.next_page()
    library.close_web()
    #library.click_selected_genre() 
    #print('resultados nuevos:',library.obtain_results())


    """Falta agregarle al método obtain_info_books un if, en el cual si una variable global está en True, este va a obtener además la descrpción de cada 
    uno de los libros, esta variable global se establece con el GUI de la palicación."""
