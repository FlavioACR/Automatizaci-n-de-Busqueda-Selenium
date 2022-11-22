# Modules & Librarys:
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
    Class that inherits unittes and performs an automation test and search for elements within the MERCADOLIBRE site.
    '''
    
    def setUp(self):
        '''
        This function prepare all the necessary to star with the Test Case.
        Parameters:
            chrome  	: import the modue  Service variable to call, save and use the path from the browser's driver.exe
            self.driver : variable to save and use the browser's driver .exe to automated our Testing Case
        Variables:
            options     :   Class for managing ChromeDriver specific options.
            chrome      :   Service class that is responsible for the starting and stopping of chromedriver the parameter is the drive´s path.
            self.driver :   We define the variable self.driver which will let us work with the driver.
            driver      :   We save the self.driver in a variable.
        '''
        options = webdriver.ChromeOptions()
        
        # We use this method to Disabling Chrome Logging Messages:
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        chrome = Service(r"C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32 106\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome, options=options)
        
        # We say to the driver wait 10 seconds before to make other actions:
        WebDriverWait(self.driver, 10)
        driver = self.driver
        
        # We use the method .get () to go to the site:
        driver.get('http://mercadolibre.com')
        
        # Maximize the window, accordingly to responsive elements that change location or order depending on the size of the view:
        driver.maximize_window()
        driver.implicitly_wait(14)

    def test_search_and_automation(self):
        '''
        Test case with a series of automated steps to enter information to the site, perform a series of filters
        identify elements within the site and save product information in a csv file.
        '''
        #e save the self.driver in a variable.
        driver = self.driver
        
        # Found the Country by id name:
        country = driver.find_element(By.ID, 'MX')
        # Click on it:
        country.click()
        sleep(1)

        # Go to the Bar and enter the search text finding it by its NAME:
        search_field = driver.find_element(By.NAME, 'as_word')
        # Click on it:
        search_field.click()
        # Clear if that has information:
        search_field.clear()
        # Write in the search bar:
        search_field.send_keys('smartphones')
        # Send the information:
        search_field.submit()
        sleep(0)
    

        # Identifies the Dropdown containing the highest or lowest priced item by its class name:
        order_menu = driver.find_element(By.CLASS_NAME, 'andes-dropdown__display-values')
        # Click on it:
        order_menu.click()
        sleep(2)
        
        # Highest Price filter identifying it by its class name:
        price_sort = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/div[1]/div/div/div/div[2]/div/div/div/div/div/ul/li[3]/div/div/span')  
        # Click on it:
        price_sort.click()
        sleep(2)

        # Empty dictionary where product information is stored:
        top_product = {}
        
        # Loop for to iterate through a range of 10 elements using the text and xpath of the elements, saving:
        # the name of the product and the price of the product:
        for i in range(10):
            article_name = driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a[1]/h2').text
            article_price = driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            top_product[article_name] = article_price

        # Using the context manager we write a .csv file with the information in the top_product dictionary:
        with open('products_tops.csv', 'w') as f:
            writer = csv.writer(f)
            for k, v in top_product.items():
                writer.writerow([k, v])                


    def tearDown(self):
        '''
        Function to close the driver or the tab
        '''
        self.driver.quit()
    

   
if __name__ == "__main__":
    # We ejecute the principal main and write the test report with testRunner:
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="MELI_Testing_reports", report_name="MELI_search_automation"))
