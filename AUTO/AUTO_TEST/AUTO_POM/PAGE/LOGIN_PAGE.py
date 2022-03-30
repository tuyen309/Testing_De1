from selenium.webdriver.common.by import By
from .LOCATORS import Locator_Login
from selenium import webdriver


class Active_Login(object):
    def __init__(self, driver):
        self.driver = driver
    def click_Sigin(self):
        self.driver.find_element(By.XPATH,(Locator_Login.sign_in_button)).click()      
    def input_email(self, email):
        self.driver.find_element(By.XPATH,(Locator_Login.input_email)).clear()
        self.driver.find_element(By.XPATH,(Locator_Login.input_email)).send_keys(email)
    def input_passwd(self, passwd):
        self.driver.find_element(By.XPATH,(Locator_Login.input_pass)).clear()
        self.driver.find_element(By.XPATH,(Locator_Login.input_pass)).send_keys(passwd)
    def click_Login(self):
        self.driver.find_element(By.XPATH,(Locator_Login.login_button)).click() 
            
            
        
