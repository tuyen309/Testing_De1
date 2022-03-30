from selenium.webdriver.common.by import By
from .LOCATORS import Locator_Register
from selenium import webdriver


class Active_Register(object):
    def __init__(self, driver):
        self.driver = driver
    def input_email_create(self, email):
        self.driver.find_element(By.XPATH,(Locator_Register.email_create)).clear()
        self.driver.find_element(By.XPATH,(Locator_Register.email_create)).send_keys(email)
    def submit_email_create(self):
        self.driver.find_element(By.XPATH,(Locator_Register.submit_create_button)).click()
