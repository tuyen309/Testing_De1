from lib2to3.pgen2 import driver
import py
from selenium import webdriver
import time
import unittest
import sys
sys.path.append("../")
from PAGE import Active_Login
from PAGE import Active_Register


#### VARIABLES####
email_register = 'tuyenntt309@gmail.com'


class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.get("http://automationpractice.com/")
    def test_login(self):
        driver = self.driver
        login = Active_Login(driver)
        login.click_Sigin()
        register = Active_Register(driver)
        register.input_email_create(email_register)
        register.submit_email_create()
        time.sleep(5)
        
        time.sleep(10)
        Verify_text = driver.find_element_by_xpath("//div[@id='center_column']/h1")
        Verify_text = Verify_text.text   
        print(Verify_text) 
        print(text_verify)
        if(Verify_text == text_verify):
            print("PASS")
        else:
            print("FAILD")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

