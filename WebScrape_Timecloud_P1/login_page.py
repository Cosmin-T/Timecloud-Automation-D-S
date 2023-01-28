import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from verify_clock_btn import check_xpath
import logging

logging.basicConfig(filename = 'error.handling.log', format = '‘%(asctime)s %(message)s' , level = logging.DEBUG)

# Custom error
class ButtonNotFound(Exception):
    pass

clock_btn = '//*[@id="clock_punch"]/div/div/ul/li[1]/div/button'
def login(driver, username, password):
    """This function is used to update the username, password and also click the login button

    Args:
        driver (WebDriver): The web driver to which the cookies will be added.
        username (STR): The username used to login
        password (STR): The password used to login
        webdriverwait (WebDriver): Finds the path of the login button and clicks it
    """
    search_box = driver.find_element(By.NAME, 'Username')
    search_box.send_keys(username)
    print('Username added successfully')
    search_box_pass = driver.find_element(By.NAME, 'PasswordView')
    search_box_pass.send_keys(password)
    print('Password added successfully')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@name = 'LoginButton']"))).click()
    print('Logged in successfully')
    time.sleep(20)

    
    