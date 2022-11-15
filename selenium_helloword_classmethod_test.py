# Modules & Librarys:
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class HelloWord(unittest.TestCase):
    '''
    This class is divided into 3 parts;
    * setUpClass: Function that prepares the driver for tests
    * TestCases: Test Cases
    * tearDownClass: Function to close the session
    
    To run the tests and the code in a single tab, the class method was added, and they were changed the 
    parameters of the 'self' functions,by the 'cls' parameter, but only in the setUps function and in the tearDown function. 	
    
    This HelloWorld test class opens two pages and generates an html report of the test results.
    '''

    @classmethod
    def setUpClass(cls):
        '''
        This function prepare all the necessary to star with the Test Case and receive as parameter the word 'cls' to use the classmethod.
            chrome = import the modue  Service variable to call, save and use the path from the browser's driver.exe
            cls.driver = variable to save and use the browser's driver .exe to automated our Testing Case
        '''
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        chrome = Service(r"C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32 106\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=chrome, options=options)

        # We say to the driver wait 10 seconds before to make other actions:
        WebDriverWait(cls.driver, 10)

    #------ HERE START THE TEST CASE ------#  

    def test_hellow_linkedin(self):
        '''
        Loads a web page in the current browser session, using the url (linkedin) as parameter
        '''
        self.driver.get("https://www.linkedin.com/feed/")
        

    def test_hellow_wiki(self):
        '''
        Loads a web page in the current browser session, using the url (wikipedia)as parameter
        '''
        self.driver.get("https://www.wikipedia.org")

    #------ HERE ENDS THE TEST CASE -------#      


    @classmethod
    def tearDownClass(cls):
        '''
        Actions to end the test case
        '''  
        cls.driver.quit()

if __name__ == "__main__":
    # Creating the html reports at the test.
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="Testing_reports", report_name="hello_word_report"))
