
#### XPATH ####
from select import select


class Locator_Login():
    my_acc = "//div[@id='center_column']/h1"
    login_button = "//button[@id='SubmitLogin']"
    input_pass = "//input[@id='passwd']"
    input_email = "//input[@id='email']"
    sign_in_button = "//a[normalize-space()='Sign in']"

class Locator_Register():
    email_create = '//div[@class="form-group"]/input[@id="email_create"]'
    submit_create_button = '//div[@class="submit"]/button[@id="SubmitCreate"]'
    checkbox_gender = '//div[@class="radio"]//input[@id="id_gender1"]'
    input_first_name = '//div[contains(@class,"required")]/input[@id="customer_firstname"]'
    input_last_name = '//div[contains(@class,"required")]/input[@id="customer_lastname"]'
    input_passwd = '//div[contains(@class,"required")]/input[@id="passwd"]'
    select_option_day = "//select[@id='days']/option[@value='10']"
    select_option_month = "//select[@id='months']/option[@value='10']"
    select_option_year = "//select[@id='years']/option[@value='1999']"
    checkbox_newsletter = '//div[@class="checkbox"]//input[@id="newsletter"]'
    checkbox_optin = '//div[@class="checkbox"]//input[@id="optin"]'
    company = '//p[@class="form-group"]/input[@id="company"]'
    address = '//p[contains(@class,"required")]/input[@id="address1"]'
    city = '//p[contains(@class,"required")]/input[@id="city"]'
    select_option_state = "//select[@id='id_state']/option[@value='10']"