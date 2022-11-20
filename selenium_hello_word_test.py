    
# Modules & Librarys:
from time import sleep
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class HelloWordOne(unittest.TestCase):
    '''
    This class is divided into 3 parts;
    * setUp: Function that prepares the driver for tests
    * TestCases: Test Cases
    * tearDown: Function to close the session
    '''    

    def setUp(self) -> None:
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

    #------ HERE START THE TEST CASE ------#  

    def test_hello_linkedin(self):
        '''
        Loads a web page in the current browser session
        
        '''
        self.driver.get("https://www.linkedin.com/feed/")
        sleep(10)
    
    #------ HERE ENDS THE TEST CASE -------#    

    def tearDown(self) -> None:
        '''
        Actions to end the test case
        ''' 
        self.driver.quit()

if __name__ == "__main__":
    # Corremos los reportes html de la prueba.
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="Testing_reports", report_name="hellow_word_test_report"))

