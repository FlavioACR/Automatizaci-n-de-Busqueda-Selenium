# lIBRERYS:

# Unittest:
import unittest
# Pyunitreport:
from pyunitreport import HTMLTestRunner
# Selenium:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# Sleep from Time:
from time import sleep
# OS:
import os
# CSV
import csv

class AutomationMELI(unittest.TestCase):
    '''
    '''
    
    def setUp(self):
        '''
        This function prepare all the necessary to star with the Test Case.
        Parameters:
            chrome  	: import the modue  Service variable to call, save and use the path from the browser's driver.exe
            self.driver : variable to save and use the browser's driver .exe to automated our Testing Case          
        '''
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome = Service(r"C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32 106\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome, options=options)
        
        # We say to the driver wait 10 seconds before to make other actions:
        WebDriverWait(self.driver, 10)

        driver = self.driver
        # Para ir al sitio:
        driver.get('http://mercadolibre.com')
        # Maximize la ventana, de acuerdo 
        # a los eleento responsivos que cambian de
        # ubicación u orden dependiendo del tamaño de la vista.
        driver.maximize_window()
        driver.implicitly_wait(14)

    def test_search_and_automation(self):
        driver = self.driver

        # Primer flujo seleccionar País:
        country = driver.find_element(By.ID, 'MX')
        country.click()
        sleep(0)

        # Ubicarse en la Barra e ingresar el texto de busqueda:
        search_field = driver.find_element(By.NAME, 'as_word')
        search_field.click()
        search_field.clear()    
        search_field.send_keys('smartphones')
        search_field.submit()
        sleep(0)
    

        # Mayor Precio filtro:
        order_menu = driver.find_element(By.CLASS_NAME, 'andes-dropdown__display-values')
        order_menu.click()
        sleep(2)
        price_sort = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/div[1]/div/div/div/div[2]/div/div/div/div/div/ul/li[3]/div/div/span')  
        price_sort.click()
        sleep(2)

        # Productos:
        top_product = {}

        for i in range(10):
            article_name = driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a[1]/h2').text
            article_price = driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            top_product[article_name] = article_price


        with open('products_tops.csv', 'w') as f:
            writer = csv.writer(f)
            for k, v in top_product.items():
                writer.writerow([k, v])                


    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="MELI_Testing_reports", report_name="MELI_search_automation"))