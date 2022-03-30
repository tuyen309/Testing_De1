from ast import If
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re
import sys
from getpass import getpass


text_verify = "My account"

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(3)
        self.base_url = "http://automationpractice.com/"
        self.verification = []
        self.accept_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click() 
        driver.find_element_by_xpath("//input[@id='email']").send_keys('nhin35443@gmail.com')
        driver.find_element_by_xpath("//input[@id='passwd']").send_keys('12345678X@x')
        driver.find_element_by_xpath("//button[@id='SubmitLogin']").click()
        time.sleep(10)


        Verify_text = driver.find_element_by_xpath("//div[@id='center_column']/h1")
        Verify_text = Verify_text.text    
        if("Verify_text" == text_verify):
            print("PASS")
        else:
            print("FAILD")
    
   
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()